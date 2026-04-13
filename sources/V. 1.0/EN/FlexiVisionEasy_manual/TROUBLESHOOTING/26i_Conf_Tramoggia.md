(troubleshooting_conf_tramoggia)=
# **Hopper Configuration**

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions

* - **Control area cannot be defined**
  - • Image not acquired

    • Wrong section selected
  - • Acquire a test image

    • Access the page through Hopper Config X


* - **AUTO does not calculate Mean and Std Dev correctly**
  - • CAPTURE operations not performed

    • CAPTURE order reversed

    • Control area too small
  - • Perform empty CAPTURE first, then full CAPTURE

    • Repeat the procedure in the correct order

    • Enlarge the control area
* - **TEST always GREEN, hopper never activates**
  - • Threshold too permissive

    • Full CAPTURE performed with too many components

    • Mean calculated incorrectly
  - • Repeat the full CAPTURE with the correct minimum number of components

    • Verify that AUTO recalculates correctly

    • Adjust the threshold manually if needed
* - **TEST always RED, hopper always activates**
  - • Threshold too restrictive

    • Empty CAPTURE performed while components were still present

  - • Repeat the empty CAPTURE with the area completely clear

    • Run AUTO again

* - **Vibration time does not produce the desired effect**
  - • Value too low

    • Value too high

    • Hopper bowl fill level varies
  - • Start from 500 ms

    • Increase or decrease by 100 ms to adjust flow

    • **CRITICAL**: keep the hopper bowl load as constant as possible

* - **Hopper discharges at the wrong time**
  - • Incorrect Steps value

    • Hopper Controller hardware not configured correctly

  - • Recalculate the Steps value

    • Check the setup specifications in the [dedicated Hopper manual]()
```
