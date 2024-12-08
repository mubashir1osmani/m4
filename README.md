crossover.ai

- product name doesnt make any sense but it will be changed later ig

## idea 

designing llm that will optimize the creation of digital systems like FPGA and ASICs

## implementation

this will prob be a terminal app, workflow goes like this: run app -> give it a prompt -> generates verilog code -> simulate using modelsim 
trained on existing llms for now: Llama, Falcon, and openAI obv
additional resources for model to train on: [Verilog/VHDL](https://github.com/klyone/opencores-ip) 

## long term vision

after gaining feedback if this project has potential, can turn into a specialized llm for EDA and chip design.
involves: 
- pretraining on a corpus of hardware design data.
- adding task specific capabilites like:
    - multi-modal input/output (eg: HDL, waveform simulation)
    - integration with GNN for layout optimization
 
do we need to create an llm?
- yes, if need highly specified knowledge in hardware design, algorithms and if existing models are not sufficient.
- no, if only need for reducing computational costs, training time. existing models can be fine-tuned

this project will be fully open source for this is a great way to learn and build something new for the future
