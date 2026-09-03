(troubleshooting_conf_tramoggia)=
# **Hopper Configuration** 
```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions

* - **Control area not definable**
  - • Image not captured
    
    • Wrong section
  - • Capture test image
    
    • Access via Config Hopper X


* - **AUTO does not calculate Mean and Std Dev correctly**
  - • CAPTURE not executed
    
    • Reverse CAPTURE order
    
    • Control area too small
  - • Run CAPTURE empty then CAPTURE full
    
    • Repeat in the correct order
    
    • Enlarge control area
* - **TEST always GREEN (hopper never switches on)**
  - • Threshold too large
    
    • CAPTURE full with too many components
    
    • Wrong calculated mean
  - • Repeat CAPTURE full with correct minimum number
    
    • Check AUTO recalculates correctly
    
    • Adjust threshold manually if necessary
* - **TEST always RED (hopper always switches on)**
  - • Threshold too restrictive
    
    • CAPTURE empty with components present
    
  - • Repeat CAPTURE empty with completely clean area
    
    • Repeat AUTO

* - **Time vibration does not produce desired effect**
  - • Value too low
    
    • Value too high 
    
    • Variable hopper tank level
  - • Start with 500ms
    
    • Increase ±100ms to adjust flow
    
    • **CRITICAL**: Maintain a constant load in the tank

* - **Hopper unloaded at wrong time**
  - • Steps not correct

    • Hopper Controller Hardware not configured properly 

  - • Recalculate Steps

    • Check the configuration specifications in the [hopper manual]() 
```

