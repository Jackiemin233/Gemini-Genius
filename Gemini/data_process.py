import os
import pickle
import config
import os

def file_search(data_path):
    file_list = []
    for home, dirs, files in os.walk(data_path):
        for f in files:
            if f.endswith('.cfg'):
                file_list.append(os.path.join(home,f))
            else:
                pass
    return file_list

def read_acfg(filepath, out_path = "dataset/data.acfg"):
    all_function_dict = {}
    with open(filepath, "rb") as f: #load i64
        picklefile = pickle.load(f)
    for func in picklefile.raw_graph_list: #read
        # if len(func.g.node) < config.min_nodes_threshold:
        #     continue
        if all_function_dict.get(func.funcname) == None:
            all_function_dict[func.funcname] = []
        all_function_dict[func.funcname].append(func.g)
    with open(out_path,"wb") as f:
        pickle.dump(all_function_dict,f)

if __name__ == '__main__':
    data_path = '/root/autodl-tmp/ACFG/Gemini/extract'
    output_path = '/root/autodl-tmp/ACFG/acfg_data'
    file_list = file_search(data_path)
    for file in file_list:
        file_name,suffix = os.path.splitext(file.split('/')[-1])
        file_name = file_name+'.acfg'#.acfg
        file_name = os.path.join(output_path,file_name) #filename
        read_acfg(filepath=file,out_path = file_name)   #preprocess