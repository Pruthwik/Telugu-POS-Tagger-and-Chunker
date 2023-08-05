# Telugu-POS-Tagger-and-Chunker
- This repository contains both Telugu pos tagger and chunker.
- Both the models are CRF based (Please install CRF++ toolkit. All the necessary details can be accesed from the below website:
https://taku910.github.io/crfpp/).
- Consists of 2 steps.
  * In the first step, extract features from the raw sentences and run the POS tagger.
  * In the second step, the chunker model is run on the output of the POS tagger, here it only depends on the pos tags, not tokens.
- How to run the models:
  * sh run_telugu_pos_and_chunk_models_and_save_to_file.sh input_file pos_model chunk_model output_file
  * You can use the sample file in the repositoty to get the output: sh run_telugu_pos_and_chunk_models_and_save_to_file.sh telugu-input.txt telugu-pos-model.m telugu-chunk-model.m telugu-output.txt
- The raw sentences need to be tokenized, for Indian language tokenization use our tokenization repository (https://github.com/Pruthwik/Tokenizer_for_Indian_Languages)

