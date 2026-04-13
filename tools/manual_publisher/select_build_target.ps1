$ErrorActionPreference = 'Stop'

Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

$repoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$sourceRoot = Join-Path $repoRoot 'sources'

function Get-VersionSortKey {
    param([string]$Label)

    $numbers = [regex]::Matches($Label, '\d+') | ForEach-Object { [int]$_.Value }
    return ,@($numbers, $Label.ToLowerInvariant())
}

function Get-SortedVersions {
    param([string]$Root)

    $versions = Get-ChildItem -LiteralPath $Root -Directory |
        Where-Object { $_.Name -notlike '_*' } |
        Select-Object -ExpandProperty Name

    return $versions | Sort-Object {
        $parts = [regex]::Matches($_, '\d+') | ForEach-Object { '{0:D8}' -f [int]$_.Value }
        (@($parts) -join '.') + '|' + $_.ToLowerInvariant()
    } -Descending
}

function Get-SortedLanguages {
    param([string]$VersionPath)

    $preferredOrder = @{
        'IT' = 0
        'EN' = 1
        'FR' = 2
        'DE' = 3
        'ES' = 4
    }

    return Get-ChildItem -LiteralPath $VersionPath -Directory |
        Where-Object { $_.Name -notlike '_*' } |
        Select-Object -ExpandProperty Name |
        Sort-Object {
            $code = $_.ToUpperInvariant()
            if ($preferredOrder.ContainsKey($code)) {
                '{0:D2}|{1}' -f $preferredOrder[$code], $code
            } else {
                '99|' + $code
            }
        }
}

$versions = Get-SortedVersions -Root $sourceRoot
if (-not $versions -or $versions.Count -eq 0) {
    throw "Nessuna versione trovata in $sourceRoot"
}

$form = New-Object System.Windows.Forms.Form
$form.Text = 'Build Manuale'
$form.StartPosition = 'CenterScreen'
$form.FormBorderStyle = 'FixedDialog'
$form.MaximizeBox = $false
$form.MinimizeBox = $false
$form.ClientSize = New-Object System.Drawing.Size(470, 325)
$form.Font = New-Object System.Drawing.Font('Segoe UI', 9)
$form.Topmost = $true

$titleLabel = New-Object System.Windows.Forms.Label
$titleLabel.Text = 'Scegli il tipo di build'
$titleLabel.Location = New-Object System.Drawing.Point(20, 18)
$titleLabel.Size = New-Object System.Drawing.Size(250, 24)
$titleLabel.Font = New-Object System.Drawing.Font('Segoe UI Semibold', 11)
$form.Controls.Add($titleLabel)

$infoLabel = New-Object System.Windows.Forms.Label
$infoLabel.Text = 'Scegli prima il tipo di build e poi se applicarlo a tutto il manuale oppure a una sola versione e lingua.'
$infoLabel.Location = New-Object System.Drawing.Point(20, 48)
$infoLabel.Size = New-Object System.Drawing.Size(420, 42)
$form.Controls.Add($infoLabel)

$typeLabel = New-Object System.Windows.Forms.Label
$typeLabel.Text = 'Tipo build'
$typeLabel.Location = New-Object System.Drawing.Point(24, 94)
$typeLabel.Size = New-Object System.Drawing.Size(100, 22)
$typeLabel.Font = New-Object System.Drawing.Font('Segoe UI Semibold', 9)
$form.Controls.Add($typeLabel)

$radioQuick = New-Object System.Windows.Forms.RadioButton
$radioQuick.Text = 'Rapido: solo HTML'
$radioQuick.Location = New-Object System.Drawing.Point(44, 118)
$radioQuick.Size = New-Object System.Drawing.Size(180, 24)
$radioQuick.Checked = $true
$form.Controls.Add($radioQuick)

$quickHint = New-Object System.Windows.Forms.Label
$quickHint.Text = 'Piu'' veloce, solo HTML.'
$quickHint.Location = New-Object System.Drawing.Point(64, 140)
$quickHint.Size = New-Object System.Drawing.Size(320, 20)
$form.Controls.Add($quickHint)

$radioFull = New-Object System.Windows.Forms.RadioButton
$radioFull.Text = 'Completo: HTML + ZIP offline'
$radioFull.Location = New-Object System.Drawing.Point(44, 166)
$radioFull.Size = New-Object System.Drawing.Size(220, 24)
$form.Controls.Add($radioFull)

$fullHint = New-Object System.Windows.Forms.Label
$fullHint.Text = 'Genera anche il pacchetto ZIP del sito offline.'
$fullHint.Location = New-Object System.Drawing.Point(64, 188)
$fullHint.Size = New-Object System.Drawing.Size(360, 20)
$form.Controls.Add($fullHint)

$scopeLabel = New-Object System.Windows.Forms.Label
$scopeLabel.Text = 'Ambito'
$scopeLabel.Location = New-Object System.Drawing.Point(24, 220)
$scopeLabel.Size = New-Object System.Drawing.Size(100, 22)
$scopeLabel.Font = New-Object System.Drawing.Font('Segoe UI Semibold', 9)
$form.Controls.Add($scopeLabel)

$radioAll = New-Object System.Windows.Forms.RadioButton
$radioAll.Text = 'Tutte le versioni e lingue'
$radioAll.Location = New-Object System.Drawing.Point(44, 244)
$radioAll.Size = New-Object System.Drawing.Size(220, 24)
$radioAll.Checked = $true
$form.Controls.Add($radioAll)

$radioSingle = New-Object System.Windows.Forms.RadioButton
$radioSingle.Text = 'Solo una versione e lingua'
$radioSingle.Location = New-Object System.Drawing.Point(44, 272)
$radioSingle.Size = New-Object System.Drawing.Size(220, 24)
$form.Controls.Add($radioSingle)

$versionLabel = New-Object System.Windows.Forms.Label
$versionLabel.Text = 'Versione'
$versionLabel.Location = New-Object System.Drawing.Point(274, 244)
$versionLabel.Size = New-Object System.Drawing.Size(80, 22)
$form.Controls.Add($versionLabel)

$versionCombo = New-Object System.Windows.Forms.ComboBox
$versionCombo.Location = New-Object System.Drawing.Point(350, 240)
$versionCombo.Size = New-Object System.Drawing.Size(95, 24)
$versionCombo.DropDownStyle = 'DropDownList'
$versionCombo.Enabled = $false
[void]$versionCombo.Items.AddRange([string[]]$versions)
$versionCombo.SelectedIndex = 0
$form.Controls.Add($versionCombo)

$languageLabel = New-Object System.Windows.Forms.Label
$languageLabel.Text = 'Lingua'
$languageLabel.Location = New-Object System.Drawing.Point(274, 274)
$languageLabel.Size = New-Object System.Drawing.Size(60, 22)
$form.Controls.Add($languageLabel)

$languageCombo = New-Object System.Windows.Forms.ComboBox
$languageCombo.Location = New-Object System.Drawing.Point(350, 270)
$languageCombo.Size = New-Object System.Drawing.Size(95, 24)
$languageCombo.DropDownStyle = 'DropDownList'
$languageCombo.Enabled = $false
$form.Controls.Add($languageCombo)

function Update-LanguageOptions {
    $languageCombo.Items.Clear()

    $selectedVersion = [string]$versionCombo.SelectedItem
    if ([string]::IsNullOrWhiteSpace($selectedVersion)) {
        return
    }

    $versionPath = Join-Path $sourceRoot $selectedVersion
    $languages = Get-SortedLanguages -VersionPath $versionPath
    if ($languages.Count -gt 0) {
        [void]$languageCombo.Items.AddRange([string[]]$languages)
        $languageCombo.SelectedIndex = 0
    }
}

function Set-SingleBuildState {
    param([bool]$Enabled)

    $versionCombo.Enabled = $Enabled
    $languageCombo.Enabled = $Enabled
}

$radioAll.Add_CheckedChanged({
    if ($radioAll.Checked) {
        Set-SingleBuildState -Enabled $false
    }
})

$radioSingle.Add_CheckedChanged({
    if ($radioSingle.Checked) {
        Set-SingleBuildState -Enabled $true
        Update-LanguageOptions
    }
})

$versionCombo.Add_SelectedIndexChanged({
    if ($radioSingle.Checked) {
        Update-LanguageOptions
    }
})

Update-LanguageOptions

$buildButton = New-Object System.Windows.Forms.Button
$buildButton.Text = 'Avvia build'
$buildButton.Location = New-Object System.Drawing.Point(254, 286)
$buildButton.Size = New-Object System.Drawing.Size(96, 32)
$buildButton.DialogResult = [System.Windows.Forms.DialogResult]::OK
$form.Controls.Add($buildButton)

$cancelButton = New-Object System.Windows.Forms.Button
$cancelButton.Text = 'Annulla'
$cancelButton.Location = New-Object System.Drawing.Point(356, 286)
$cancelButton.Size = New-Object System.Drawing.Size(96, 32)
$cancelButton.DialogResult = [System.Windows.Forms.DialogResult]::Cancel
$form.Controls.Add($cancelButton)

$form.AcceptButton = $buildButton
$form.CancelButton = $cancelButton

$result = $form.ShowDialog()

if ($result -ne [System.Windows.Forms.DialogResult]::OK) {
    Write-Output 'CANCELLED=1'
    exit 0
}

if ($radioSingle.Checked) {
    $selectedVersion = [string]$versionCombo.SelectedItem
    $selectedLanguage = [string]$languageCombo.SelectedItem

    if ([string]::IsNullOrWhiteSpace($selectedVersion) -or [string]::IsNullOrWhiteSpace($selectedLanguage)) {
        [System.Windows.Forms.MessageBox]::Show(
            'Seleziona una versione e una lingua valide.',
            'Selezione incompleta',
            [System.Windows.Forms.MessageBoxButtons]::OK,
            [System.Windows.Forms.MessageBoxIcon]::Warning
        ) | Out-Null
        Write-Output 'CANCELLED=1'
        exit 0
    }

    if ($radioFull.Checked) {
        Write-Output 'BUILD_TYPE=full'
    } else {
        Write-Output 'BUILD_TYPE=quick'
    }
    Write-Output 'BUILD_SCOPE=single'
    Write-Output ('VERSION=' + $selectedVersion)
    Write-Output ('LANGUAGE=' + $selectedLanguage)
    exit 0
}

if ($radioFull.Checked) {
    Write-Output 'BUILD_TYPE=full'
} else {
    Write-Output 'BUILD_TYPE=quick'
}
Write-Output 'BUILD_SCOPE=all'
