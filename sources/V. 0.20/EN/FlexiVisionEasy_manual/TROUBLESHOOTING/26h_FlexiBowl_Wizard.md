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
    
    • Check FlexiBowl connection
    
    • Complete basic system configuration

* - **Set rotation direction does not match**
  - • CW/CCW selection error
    
  - • Visually verify the actual rotation direction
    
    • Correct the selection in the Wizard
    
* - **Air-blow test does not work**
  - • Compressed air not connected
    
    • Insufficient pressure
    
    • Module not physically present
  - • Check compressed-air connection
    
    • Increase pressure to 5-6 bar
    
    • Select "FlexiBowl NOT equipped" if the module is absent
* - **Flip test not noticeable**
  - • Compressed air not connected/insufficient
    
    • Pressure regulator closed
    
    • Pneumatic circuit leaks
  - • Verify compressed air is connected
    
    • Open regulator on control panel
    
    • Verify pressure 5-6 bar
    
    • Inspect fittings for leaks
* - **Calculated parameters not optimal**
  - • Incorrect component characterization
    
    • Wizard uses generic values
  - • Review selected geometry and behavior
    
    • Accept Wizard parameters as a starting point
    
    • Fine-tune manually in the summary dashboard

* - **Components move during acquisition**
  - • Speed/acceleration too high
    
    • Stabilization pauses absent
    
    • Grip surface not suitable
  - • Decrease Speed and Accel
    
    • Insert 200-500ms pauses
    
    • Replace grip surface with a more adhesive one
* - **Air blow not effective**
  - • Air pressure insufficient/excessive
    
    • Nozzles clogged
  - • Verify pressure 5-6 bar
    
    • Clean air-blow nozzles

* - **Parameter changes are not applied**
  - • "Synchronize Parameters" not pressed
    
    • Recipe not saved
  - • **ALWAYS** click Synchronize Parameters after changes
    
    • Save recipe to make changes permanent
* - **Turn FLB does not work during setup**
  - • FlexiBowl not connected
    
    • Command not configured
    
    • FlexiBowl in error
  - • Check FlexiBowl connection
    
    • Check FlexiBowl Setup configuration
    
    • Check FlexiBowl READY LED
```
