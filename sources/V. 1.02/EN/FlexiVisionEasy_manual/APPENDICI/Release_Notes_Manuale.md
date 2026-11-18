# Manual FlexiVision One

This page collects the revision history of this manual and indicates which versions of the FlexiVision One software each revision is compatible with.

```{important}
Always consult the manual version that is compatible with the installed software version to access the most up-to-date information on features, safety and procedures.
```

## Compatibility

| Manual version | Compatible FlexiVision One software versions |
|---|---|
| **1.02** (current) | v0.23, v0.24 |
| **1.01** | v0.21, v0.22 |
| **1.00** | v0.20, v0.21, v0.22 |

## Revision history

### Version 1.02

Publication date: 17 November 2026

**Pages added**

- New **Control Cameras** section, with the pages:
  - [Control Cameras](../TELECAMERE_CONTROLLO/33_Telecamere_Controllo.md): overview, operating sequence, use from the HMI (Setup Camera Ctrl, Setup Tool Ctrl, View Runtime, Test Tool) and quick acceptance test.
  - [`start_control_` command](../TELECAMERE_CONTROLLO/34_Comando_start_control.md): command format, parameters, responses to the robot and example exchanges.
  - [VisionPro Script](../TELECAMERE_CONTROLLO/35_Script_VisionPro.md): ToolBlock interface, script customization and Appendix A with the complete C# script.
- Added the page [Troubleshooting – Control Cameras](../TROUBLESHOOTING/26j_Telecamere_Controllo.md) with the `#Error_Control_…` and `#Error_Camera…` messages and recommended actions.
- All the pages of the Control Cameras section show a banner at the top indicating that the **Control Camera** is an **Expert** function.

**Pages updated**

- [Robot-Vision Communication Protocol](../rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md): added the subsection "Control camera commands" with the `start_control_<parameter>` command.
- [Troubleshooting](../TROUBLESHOOTING/26_trb_shooting_guide.md): added the "Control Cameras" card.
- [Glossary](../27b_Glossario.md): added the terms CogRecord, PMRedLine, Control Camera, ToolBlock and VisionPro.
- Release Notes – Software: added the versions [V. 0.23](V.0.23.md) and [V. 0.24](V.0.24.md) and updated the [FlexiVision One Software](Release_Notes_Software.md) page.
- Updated the compatibility table with the software versions v0.23 and v0.24.

### Version 1.01

Publication date: 4 September 2026

- Added the **Check Belt** page (Disk Monitoring) to the Quickstart, and the related entry in the Setup page of the Interface Overview.
- Updated the Hopper Setup section with the **Wizard Steps** and **Wizard Time** guided procedures.
- Updated the Histograms section with the choice of region type for Clearances (Rectangle, Annulus Section, Circle).
- Updated the Mix Applications section with the multi-model `mix_Locator_<models>` commands and the protection for commands already running.
- Added the subsection "How to use the Start and Mix commands correctly" to the Robot-Vision Communication Protocol.
- Updated the FlexiBowl® Setup section: manual keyboard entry of parameters and a warning when parameters are not synchronized.
- Updated the Robot Pick section: offset format with the dot as decimal separator and a check on the Picking Offset before proceeding with **Next**.
- Added to the Setup section the note on the user access level check.
- Reorganized the Release Notes section, separating the FlexiVision One software notes from the manual notes.

### Version 1.00

Publication date: 1 August 2026

- First edition of the manual.
