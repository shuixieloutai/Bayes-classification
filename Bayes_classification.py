class Classifier:
    def  __init__(self):
        self.metas_num=0
        self.metas=[]
        
    def load_meta(self, file_path):
        with open(file_path) as f:
            self.lines=f.readlines()
        self.metas_num=len(self.lines)-1
        for line in self.lines:
            #self.meta.append([line.split(':')[0], line.split(':',1)[1].replace('\n','').split(',')])
            self.metas.append(line.replace('\n','').replace(':',',').split(','))
            #self.meta_class.append()
            
    def load_train(self, file_path):
        with open(file_path) as f:
            lines=f.readlines()
        self.data_train=[]
        for line in lines:
            self.data_train.append(line.replace('\n','').split(','))
            
    def load_test(self, file_path):
        with open(file_path) as f:
            lines=f.readlines()
        self.data_test=[]
        for line in lines:
            self.data_test.append(line.replace('\n','').split(','))
            
    def save(self, file_path):
        with open(file_path, 'w') as f:
            for data in self.data_evaluate:
                sentence=''
                for i in range(len(data)):
                    sentence=sentence+data[i]
                    if i < len(data)-1:
                         sentence=sentence+','
                sentence=sentence+'\n'
                f.write(sentence)
            
    def count_num(self):
        self.count=dict()
        for clas in self.metas[-1][1:]:
            self.count[clas]=dict()
            for i in range(self.metas_num):
                meta=self.metas[i]
                #print(meta)
                self.count[clas][meta[0]]=dict()
                for word in meta[1:]:
                    c=0
                    for data in self.data_train:
                        if data[i]==word and data[-1]==clas:
                            c+=1
                    self.count[clas][meta[0]][word]=c
                
    def cal_base_rates(self):
        self.base_rates = {}
        self.base_count = {}
        for clas in self.count:
            c=0
            for i in self.count[clas][list(self.count[clas].keys())[0]]:
                c+=self.count[clas][list(self.count[clas].keys())[0]][i]
            self.base_count[clas]=c
            self.base_rates[clas]=c/len(self.data_train)
        
    def cal_pro(self):
        self.pro=dict()
        for clas in self.count:
            self.pro[clas]=dict()
            for meta in self.count[clas]:
                self.pro[clas][meta]=dict()
                for meta_class in self.count[clas][meta]:
                    v=len(self.count[clas][meta])
                    self.pro[clas][meta][meta_class]=(self.count[clas][meta][meta_class]+1)/(self.base_count[clas]+v)
                    
    def train(self, file_path_meta, file_path_train):
        self.load_meta(file_path_meta)
        
        self.load_train(file_path_train)
        
        self.count_num()
        
        self.cal_base_rates()
        
        self.cal_pro()
        
    def pre_data(self, data):
        p_max=-1
        key_max=-1
        for key in list(self.pro.keys()):
            p=self.base_rates[key]  
            for i in range(self.metas_num):
                #print(classifier.data_test[0][i])
                #print(classifier.pro['unacc'][classifier.metas[i][0]][classifier.data_test[0][i]])
                p=p*self.pro[key][self.metas[i][0]][data[i]]
            p=p
            if p>p_max:
                p_max=p
                key_max=key
        return key_max, p_max
    
    def evaluate(self, file_path):
        self.load_test(file_path)
        count=0
        for data in self.data_test:
            key_max, p_max=self.pre_data(data)
            if key_max == data[-1]:
                count+=1
        acc=count/len(self.data_test)
        print("acc:",acc)
        return acc
    
    def predict(self, file_path_input, file_path_output):
        self.data_evaluate=[]
        self.load_test(file_path_input)
        #print(self.data_test)
        for i in range(len(self.data_test)):
            data=self.data_test[i]
            #print(data)
            key_max, p_max=self.pre_data(data)
            if len(data)==self.metas_num:
                data.append(key_max)
            else:
                #print(key_max,data[-1])
                data[-1]=key_max
            self.data_evaluate.append(data)
        self.save(file_path_output)