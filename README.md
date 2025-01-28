
## idea 

utilize agents to create chips and custom FPGAs and ASICs

## implementation

workflow: system prompt -> user specifications for chip -> generates verilog code / simulation of how it works -> use modelsim for testing <- reiterate
additional resources for model to train on: [Verilog/VHDL](https://github.com/klyone/opencores-ip) 

## long term vision

after gaining feedback if this project has potential, can turn into a specialized product for EDA and chip design.
involves: 
- pretraining on a corpus of hardware design data.
- adding task specific capabilites like:
    - multi-modal input/output (eg: HDL, waveform simulation)
    - integration with GNN for layout optimization
 
this project will be fully open source for this is a great way to learn and build something new for the future
