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
    
    • Wrong section
  - • Acquire test image
    
    • Access through Config Hopper X


* - **AUTO does not calculate Mean and Std Dev correctly**
  - • CAPTURE not performed
    
    • CAPTURE order reversed
    
    • Control area too small
  - • Perform empty CAPTURE then full CAPTURE
    
    • Repeat in the correct order
    
    • Enlarge the control area
* - **TEST always GREEN (hopper never activates)**
  - • Threshold too permissive
    
    • Full CAPTURE with too many components
    
    • Incorrect calculated Mean
  - • Repeat full CAPTURE with the correct minimum number
    
    • Verify that AUTO recalculates correctly
    
    • Manually adjust the threshold if necessary
* - **TEST always RED (hopper always activates)**
  - • Threshold too restrictive
    
    • Empty CAPTURE with components present
    
  - • Repeat empty CAPTURE with a completely clean area
    
    • Repeat AUTO

* - **Vibration time does not produce the desired effect**
  - • Value too low
    
    • Value too high 
    
    • Variable hopper bowl level
  - • Start with 500ms
    
    • Increase by ±100ms to adjust the flow
    
    • **CRITICAL**: Maintain a constant load in the bowl

* - **Hopper discharges at the wrong times**
  - • Incorrect Steps

    • Hopper Controller hardware not configured correctly 

  - • Recalculate Steps

    • Check the configuration specifications in the [dedicated Hopper manual]() 
```

