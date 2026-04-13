(troubleshooting_fb_wizard)=
# **FlexiBowl Wizard**

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions
* - **Wizard does not start**
  - • Recipe not loaded

    • FlexiBowl not connected

    • Initial setup not completed
  - • Load or create a recipe first

    • Verify the FlexiBowl connection

    • Complete the basic system configuration

* - **Configured rotation direction does not match actual direction**
  - • Incorrect CW or CCW selection

  - • Visually verify the actual rotation direction

    • Correct the selection inside the Wizard

* - **Air-blow test does not work**
  - • Compressed air not connected

    • Insufficient pressure

    • Module not physically installed
  - • Verify the compressed air connection

    • Increase pressure to 5-6 bar

    • Select `"FlexiBowl NOT equipped"` if the module is absent
* - **Flip test is not noticeable**
  - • Compressed air not connected or insufficient

    • Pressure regulator closed

    • Leaks in the pneumatic circuit
  - • Verify that compressed air is connected

    • Open the regulator on the control panel

    • Verify pressure at 5-6 bar

    • Inspect fittings for leaks
* - **Calculated parameters are not optimal**
  - • Incorrect component characterization

    • Wizard uses generic values
  - • Review the selected geometry and behavior

    • Accept the Wizard parameters as a starting point

    • Fine-tune them manually in the summary dashboard

* - **Components move during image acquisition**
  - • Speed or acceleration too high

    • No stabilization pause

    • Grip surface not suitable
  - • Reduce Speed and Accel

    • Add pauses of 200-500 ms

    • Replace the grip surface with a more suitable one
* - **Air blow is not effective**
  - • Air pressure insufficient or excessive

    • Nozzles clogged
  - • Verify pressure at 5-6 bar

    • Clean the air-blow nozzles

* - **Parameter changes are not applied**
  - • `"Synchronize Parameters"` not pressed

    • Recipe not saved
  - • **ALWAYS** click **Synchronize Parameters** after modifications

    • Save the recipe to make the changes permanent
* - **Turn FLB does not work during setup**
  - • FlexiBowl not connected

    • Command not configured

    • FlexiBowl in error
  - • Verify the FlexiBowl connection

    • Check the FlexiBowl Setup configuration

    • Verify the FlexiBowl READY LED
```
