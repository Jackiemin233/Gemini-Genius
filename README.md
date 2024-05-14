# usage

1. Please refer the https://github.com/Yunlongs/Genuis generate the dataset and preprocess it.
```
python Gemini_data_1.py
```

2. Modify the path in config.py and train the model:
```
python Gemini_train_2.py
```

3. Download the IDA Pro 7.7 from the Baidu.

Link：https://pan.baidu.com/s/19PfekgQ1AyElpH0EXZT_Xg?pwd=ex37 
pwd：ex37 

4. After installing the IDA Pro 7.7. Move the /IDA_appendix/idc_bc695.py to path/to/yourIDA/python/3.

5. Modify the PATH in batch_run.py and preprocessing_ida to generate the .cfg file.
```
python batch_run.py
```
6. Refer to APIs in  similarity_inference.py to infer the .acfg file 
(TRUST ME! VERY EASY TO READ AND USE)

Big Thanks to Yunlongs's Contribution!