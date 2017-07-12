'''
Created on 2017. 7. 11.

@author: Altang
'''

import pandas as pd
import glob
import os, shutil, operator
from sklearn import preprocessing

def dfNormalization(df):
    x = df.values #returns a numpy array
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    normdf = pd.DataFrame(x_scaled)
    
    return normdf


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def removeFiles(folder):
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
                
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)

def dongNameChange(filteredData, old_name, new_name):
    indexList = filteredData.index.tolist()
    
    if old_name in indexList:             
        indexList[indexList.index(old_name)] = new_name
        filteredData.index = indexList

def getPandasDataFrame(fname):
    
    fwname = fname.split("\\")[-1].replace(".xls", ".csv")
    data = pd.read_excel(fname, encoding="euc-kr")
         
    header = [0]
    try:
        filteredData = data[data['Period'].str.contains("Period") == True]             
        header = list(range(len(filteredData) + 1))
        # print(fname, len(filteredData))
    except:           
        pass 
        
    print(fname, header)
        
    try:
        
        data = pd.read_excel(fname, encoding="euc-kr", header=header)
        indexed_data = None
        for column in data.columns:
            if "Dong" in column:
                indexed_data = data.set_index(column)
                indexed_data.index.name = "Dong"
                break
        
        filteredData = indexed_data[indexed_data.index.str.contains("dong") == True]
        
        if len(header) > 1:        
            filteredData.columns = ["%s_%s" % (fwname.replace(".csv", ""), "_".join(column)) for column in filteredData.columns]
        else:
            filteredData.columns = ["%s_%s" % (fwname.replace(".csv", ""), column) for column in filteredData.columns]
        
        dongNameChange(filteredData, "Myeongdong", "Myeong-dong")
        dongNameChange(filteredData, "Sindang 1(il)-dong", "Sindang-dong")
        dongNameChange(filteredData, "Sindang 2(i)-dong", "Dasan-dong")
        dongNameChange(filteredData, "Sindang 3(sam)-dong", "Yaksu-dong")
        dongNameChange(filteredData, "Sindang 4(sa)-dong", "Cheonggu-dong")
        dongNameChange(filteredData, "Sindang 6(yuk)-dong", "Donghwa-dong")
        
        filteredData.index.name = "Dong"
            
        fs = fwname.split("_")
        folder = fs[0]
        fname = "_".join(fs[1:])
        
        if not os.path.isdir("../data/clean_stat/%s" % folder):
            os.mkdir("../data/clean_stat/%s" % folder)
            
        filteredData.to_csv("../data/clean_stat/%s/%s" % (folder, fname))
    except:  
        raise      
        print(fname, "error")        
        return None
    
    return filteredData

def cleanStatFiles():
    filelist = glob.glob("../data/17_동별통계자료/*.xls")
    
    targetPath = "../data/clean_stat"
    removeFiles(targetPath)
    dongDict = {}
    
    mergedData = None
    
    for fname in filelist:
        data = getPandasDataFrame(fname)
        
def mergeCSVFiles():
    
    dongList = ["Sajik-dong", "Samcheong-dong", "Buam-dong", "Pyeongchang-dong", "Muak-dong", "Gyonam-dong", "Gahoe-dong", "Jongno 1·2·3·4(ilisamsa)-ga-dong", "Jongno 5·6(oryuk)-ga-dong", "Ihwa-dong", "Changsin 1(il)-dong", "Changsin 2(i)-dong", "Changsin 3(sam)-dong", "Sungin 1(il)-dong", "Sungin 2(i)-dong", "Cheongunhyoja-dong", "Hyehwa-dong", "Sogong-dong", "Hoehyeon-dong", "Myeong-dong", "Pil-dong", "Jangchung-dong", "Gwanghui-dong ", "Euljiro-dong", "Sindang 5(o)-dong", "Hwanghak-dong", "Jungnim-dong", "Sindang-dong", "Dasan-dong", "Yaksu-dong", "Cheonggu-dong", "Donghwa-dong", "Huam-dong", "Yongsan 2-ga-dong", "Namyeong-dong", "Wonhyoro 2(i)-dong", "Hyochang-dong", "Yongmun-dong", "Ichon 1(il)-dong", "Ichon 2(i)-dong", "Itaewon 1(il)-dong", "Itaewon 2(i)-dong", "Seobinggo-dong", "Bogwang-dong", "Cheongpa-dong", "Wonhyoro 1(il)-dong", "Hangangno-dong", "Hannam-dong", "Wangsimni 2(i)-dong", "Majang-dong", "Sageun-dong", "Haengdang 1(il)-dong", "Haengdang 2(i)-dong", "Eungbong-dong", "Geumho 1(il)-ga-dong", "Geumho 4(sa)-ga-dong", "Seongsu 1(il)-ga1(il)-dong", "Seongsu 1(il)-ga2(i)-dong", "Seongsu 2(i)-ga1(il)-dong", "Seongsu 2(i)-ga 3(sam)-dong", "Songjeong-dong", "Yongdap-dong", "WangsimniDoseon-dong", "Geumho 2.3(i.sam)-ga-dong", "Oksu-dong", "Hwayang-dong", "Gunja-dong", "Junggok 1(il)-dong", "Junggok 2(i)-dong", "Junggok 3(sam)-dong", "Junggok 4(sa)-dong", "Neung-dong", "Guui 1(il)-dong", "Guui 2(i)-dong", "Guui 3(sam)-dong", "Gwangjang-dong", "Jayang 1(il)-dong", "Jayang 2(i)-dong", "Jayang 3(sam)-dong", "Jayang 4(sa)-dong", "Hoegi-dong", "Hwigyeong 1(il)-dong", "Hwigyeong 2(i)-dong", "Cheongnyangni-dong", "Yongsin-dong", "Jegi-dong", "Jeonnong 1(il)-dong", "Jeonnong 2(i)-dong", "Dapsimni 1(il)-dong", "Dapsimni 2(i)-dong", "Jangan 1(il)-dong", "Jangan 2(i)-dong", "Imun 1(il)-dong", "Imun 2(i)-dong", "Myeonmok 2(i)-dong", "Myeonmok 4(sa)-dong", "Myeonmok 5(o)-dong", "Myeonmok 7(chil)-dong", "Sangbong 1(il)-dong", "Sangbong 2(i)-dong", "Junghwa 1(il)-dong", "Junghwa 2(i)-dong", "Muk 1(il)-dong", "Muk 2(i)-dong", "Mangu 3(sam)-dong", "Sinnae 1(il)-dong", "Sinnae 2(i)-dong", "Myeonmokbon-dong", "Myeonmok 3.8(sam.pal)-dong", "Mangubon-dong", "Donam 1(il)-dong", "Donam 2(i)-dong", "Anam-dong", "Bomun-dong", "Jeongneung 1(il)-dong", "Jeongneung 2(i)-dong", "Jeongneung 3(sam)-dong", "Jeongneung 4(sa)-dong", "Gireum 1(il)-dong", "Gireum 2(i)-dong", "Wolgok 1(il)-dong", "Wolgok 2(i)-dong", "Jangwi 1(il)-dong", "Jangwi 2(i)-dong", "Jangwi 3(sam)-dong", "Seongbuk-dong", "Samseon-dong", "Dongseon-dong", "Jongam-dong", "Seokgwan-dong", "Beon 1(il)-dong", "Beon 2(i)-dong", "Beon 3(sam)-dong", "Suyu 1(il)-dong", "Suyu 2(i)-dong", "Suyu 3(sam)-dong", "Samyang-dong", "Mia-dong", "Songjung-dong", "Songcheon-dong", "Samgaksan-dong", "Ui-dong", "Insu-dong", "Ssangmun 1(il)-dong", "Ssangmun 2(i)-dong", "Ssangmun 3(sam)-dong", "Ssangmun 4(sa)-dong", "Banghak 1(il)-dong", "Banghak 2(i)-dong", "Banghak 3(sam)-dong", "Chang 1(il)-dong", "Chang 2(i)-dong", "Chang 3(sam)-dong", "Chang 4(sa)-dong", "Chang 5(o)-dong", "Dobong 1(il)-dong", "Dobong 2(i)-dong", "Wolgye 1(il)-dong", "Wolgye 2(i)-dong", "Wolgye 3(sam)-dong", "Gongneung 2(i)-dong", "Hagye 1(il)-dong", "Hagye 2(i)-dong", "Junggyebon-dong", "Junggye 1(il)-dong", "Junggye 4(sa)-dong", "Sanggye 1(il)-dong", "Sanggye 2(i)-dong", "Sanggye 5(o)-dong", "Sanggye 8(pal)-dong", "Sanggye 9(gu)-dong", "Sanggye 10(sip)-dong", "Sanggye 3.4(sam.sa)-dong", "Sanggye 6.7(yuk.chil)-dong", "Junggye 2.3(i.sam)-dong", "Gongneung 1(il)-dong", "Nokbeon-dong", "Bulgwang 1(il)-dong", "Galhyeon 1(il)-dong", "Galhyeon 2(i)-dong", "Gusan-dong", "Daejo-dong", "Eungam 1(il)-dong", "Eungam 2(i)-dong", "Sinsa 1(il)-dong", "Sinsa 2(i)-dong", "Jeungsan-dong", "Susaek-dong", "Jingwan-dong", "Bulgwang 2(i)-dong", "Eungam 3(sam)-dong", "Yeokchon-dong", "Cheonyeon-dong", "Hongje 1(il)-dong", "Hongje 3(sam)-dong", "Hongje 2(i)-dong", "Hongeun 1(il)-dong", "Hongeun 2(i)-dong", "Namgajwa 1(il)-dong", "Namgajwa 2(i)-dong", "Bukgajwa 1(il)-dong", "Bukgajwa 2(i)-dong", "Chunghyeon-dong", "Bugahyeon-dong", "Sinchon-dong", "Yeonhui-dong", "Yonggang-dong", "Daeheung-dong", "Yeomni-dong", "Sinsu-dong", "Seogyo-dong", "Hapjeong-dong", "Mangwon 1(il)-dong", "Mangwon 2(i)-dong", "Yeonnam-dong", "Seongsan 1(il)-dong", "Seongsan 2(i)-dong", "Sangam-dong", "Dohwa-dong", "Seogang-dong", "gongdeok-dong", "Ahyeon-dong", "Mok 1(il)-dong", "Mok 2(i)-dong", "Mok 3(sam)-dong", "Mok 4(sa)-dong", "Sinwol 1(il)-dong", "Sinwol 2(i)-dong", "Sinwol 3(sam)-dong", "Sinwol 4(sa)-dong", "Sinwol 5(o)-dong", "Sinwol 6(yuk)-dong", "Sinwol 7(chil)-dong", "Sinjeong 1(il)-dong", "Sinjeong 2(i)-dong", "Sinjeong 3(sam)-dong", "Sinjeong 6(yuk)-dong", "Sinjeong 7(chil)-dong", "Mok 5(o)-dong", "Sinjeong 4(sa)-dong", "Yeomchang-dong", "Deungchon 1(il)-dong", "Deungchon 2(i)-dong", "Deungchon 3(sam)-dong", "Hwagokbon-dong", "Hwagok 2(i)-dong", "Hwagok 3(sam)-dong", "Hwagok 4(sa)-dong", "Hwagok 6(yuk)-dong", "Hwagok 8(pal)-dong", "Gayang 1(il)-dong", "Gayang 2(i)-dong", "Gayang 3(sam)-dong", "Balsan 1(il)-dong", "Gonghang-dong", "Banghwa 1(il)-dong", "Banghwa 2(i)-dong", "Banghwa 3(sam)-dong", "Hwagok 1(il)-dong", "Ujangsan-dong", "Sindorim-dong", "Guro 1(il)-dong", "Guro 3(sam)-dong", "Guro 4(sa)-dong", "Guro 5(o)-dong", "Gocheok 1(il)-dong", "Gocheok 2(i)-dong", "Gaebong 2(i)-dong", "Gaebong 3(sam)-dong", "Oryu 1(il)-dong", "Oryu 2(i)-dong", "Sugung-dong", "Garibong-dong", "Guro 2(i)-dong", "Gaebong 1(il)-dong", "Gasan-dong", "Doksan 1(il)-dong", "Doksan 2(i)-dong", "Doksan 3(sam)-dong", "Doksan 4(sa)-dong", "Siheung 1(il)-dong", "Siheung 2(i)-dong", "Siheung 3(sam)-dong", "Siheung 4(sa)-dong", "Siheung 5(o)-dong", "Yeouido-dong", "Dangsan 1(il)-dong", "Dangsan2(i)-dong", "Yangpyeong 1(il)-dong", "Yangpyeong 2(i)-dong", "Singil 1(il)-dong", "Singil 3(sam)-dong", "Singil 4(sa)-dong", "Singil 5(o)-dong", "Singil 6(yuk)-dong", "Singil 7(chil)-dong", "Daerim 1(il)-dong", "Daerim 2(i)-dong", "Daerim 3(sam)-dong", "Yeongdeungpobon-dong", "Yeongdeungpo-dong", "Dorim-dong", "Mullae-dong", "Noryangjin 2(i)-dong", "Sangdo 1(il)-dong", "Sangdo 2(i)-dong", "Sangdo 3(sam)-dong", "Sangdo 4(sa)-dong", "Sadang 1(il)-dong", "Sadang 3(sam)-dong", "Sadang 4(sa)-dong", "Sadang 5(o)-dong", "Daebang-dong", "Sindaebang 1(il)-dong", "Sindaebang 2(i)-dong", "Heukseok-dong", "Noryangjin 1(il)-dong", "Sadang 2(i)-dong", "Boramae-dong", "Cheongnim-dong", "Haengun-dong", "Nagseongdae-dong", "Jungang-dong", "Inheon-dong", "Namhyeon-dong", "Sewon-dong", "Sinwon-dong", "Serim-dong", "Sinsa-dong", "Sillim-dong", "Nanhyang-dong", "Jowon-dong", "Daehak-dong", "Euncheon-dong", "Seonghyeon-dong", "Cheongnyong-dong", "Nangok-dong", "Samseong-dong", "Miseong-dong", "Seocho 1(il)-dong", "Seocho 2(i)-dong", "Seocho 3(sam)-dong", "Seocho 4(sa)-dong", "Jamwon-dong", "Banpobon-dong", "Banpo 1(il)-dong", "Banpo 2(i)-dong", "Banpo 3(sam)-dong", "Banpo 4(sa)-dong", "Bangbaebon-dong", "Bangbae 1(il)-dong", "Bangbae 2(i)-dong", "Bangbae 3(sam)-dong", "Bangbae 4(sa)-dong", "Yangjae 1(il)-dong", "Yangjae 2(i)-dong", "Naegok-dong", "Sinsa-dong", "Nonhyeon 1(il)-dong", "Nonhyeon 2(i)-dong", "Samseong 1(il)-dong", "Samseong 2(i)-dong", "Daechi 1(il)-dong", "Daechi 4(sa)-dong", "Yeoksam 1(il)-dong", "Yeoksam 2(i)-dong", "Dogok 1(il)-dong", "Dogok 2(i)-dong", "Gaepo 1(il)-dong", "Gaepo 4(sa)-dong", "Irwonbon-dong", "Irwon 1(il)-dong", "Irwon 2(i)-dong", "Suseo-dong", "Segok-dong", "Apgujeong -dong", "Cheongdam -dong", "Daechi 2(i)-dong", "Gaepo 2(i)-dong", "Pungnap 1(il)-dong", "Pungnap 2(i)-dong", "Geoyeo 1(il)-dong", "Geoyeo 2(i)-dong", "Macheon 1(il)-dong", "Macheon 2(i)-dong", "Bangi 1(il)-dong", "Bangi 2(i)-dong", "Oryun-dong", "Ogeum-dong", "Songpa 1(il)-dong", "Songpa 2(i)-dong", "Seokchon-dong", "Samjeon-dong", "Garakbon-dong", "Garak 1(il)-dong", "Garak 2(i)-dong", "Munjeong 1(il)-dong", "Munjeong 2(i)-dong", "Jangji-dong", "Jamsilbon-dong", "Jamsil 4(sa)-dong", "Jamsil 6(yuk)-dong", "Jamsil 7(chil)-dong", "Jamsil 2(i)-dong", "Jamsil 3(sam)-dong", "Gangil-dong", "Sangil-dong", "Myeongil 1(il)-dong", "Myeongil 2(i)-dong", "Godeok 1(il)-dong", "Godeok 2(i)-dong", "Amsa 2(i)-dong", "Amsa 3(sam)-dong", "Cheonho 1(il)-dong", "Cheonho 3(sam)-dong", "Seongnae 1(il)-dong", "Seongnae 2(i)-dong", "Seongnae 3(sam)-dong", "Dunchon 1(il)-dong", "Dunchon 2(i)-dong", "Amsa 1(il)-dong", "Cheonho 2(i)-dong", "Gil-dong"]
    allfolders = glob.glob("..\\data\\clean_stat\\*")
    
    totalDict = {}
    keyList = []
    
    for folder in allfolders:
        
        fwname = folder.split("\\")[-1]
        allFiles = glob.iglob("%s\\*.csv" % folder)
        
        for file_ in allFiles:
            
            df = pd.read_csv(file_, encoding="euc-kr", header=0)
            
            if len(df.index) != 423:
                print(file_, len(df.index))
            
            for key in df.columns:
                if "Gu" in key or "Period" in key or "Dong" in key:                                            
                    continue
                keyList.append(key)
            
            for index, row in df.iterrows():                
                rowDict = row.to_dict()
                
                dong = rowDict.pop("Dong")
                
                if dong not in totalDict:
                    totalDict[dong] = {}
                
                totalDict[dong].update(rowDict)
        
    with open("../data/merged_stat/%s.csv" % "total", "w") as fw:
        writeKeyList = [key.replace(",", ".") for key in keyList]
        fw.write("Dong,%s\n" % ",".join(writeKeyList))

        for dong in dongList:            
            fw.write(dong)                
            if dong in totalDict:
                for key in keyList:
                    if key in totalDict[dong]:               
                        
                        
                        if is_number(str(totalDict[dong][key])): 
                            fw.write(",%s" % totalDict[dong][key])
                        else:                            
                            fw.write(",None")
                        
                    else:
                        fw.write(",None")
                                            
            else:
                for key in keyList:
                    fw.write(",None")
                                        
            fw.write("\n")      
            
def tooManyNone(x):
    
    counts = x.value_counts()
    limit = 0
    
    if 'None' in counts and counts['None'] > limit:        
        return False
    else:        
        return True
            
def removeInvalidData():
    
    fname = "../data/merged_stat/total.csv"
    data = pd.read_csv(fname, encoding="euc-kr", index_col=0)                  
    newdata = data.loc[:, data.apply(tooManyNone)]
    
    
    cordata = newdata.corr().abs()
    s = cordata.unstack()
    #print(s)
    #so = s.order(kind="quicksort")
    
    dupDict = {}
    groupCount = 0
    
    for k,v in s.to_dict().items():
        if v == 1 and k[0] != k[1]:
            sortedKey = sorted(k)
            
            if sortedKey[0] not in dupDict and sortedKey[1] not in dupDict:
                dupDict[sortedKey[0]] = groupCount
                dupDict[sortedKey[1]] = groupCount
                groupCount += 1
    
    sorted_dupDict = sorted(dupDict.items(), key=operator.itemgetter(1))

    invalidList = []
    validList = []
    
    currentCount = -1
    for k,v in sorted_dupDict:
        if currentCount != v:
            currentCount += 1
            validList.append(k)
            continue
        invalidList.append(k)
    
    result = newdata.drop(invalidList, axis=1)
    result = dfNormalization(result)
    print(len(result.columns))
    result.to_csv("../output/function1_data.csv")
    
    cordata = result.corr().abs()
    s = cordata.unstack()
    
    highcor = s.loc[s==1,:]
    highcor = highcor.loc[highcor<1,:]    
    highcor.to_csv("../output/function1_cor.csv")
    
    
    #highcor.to_csv("cor.csv")
    
if __name__ == '__main__':
    #cleanStatFiles()
    #mergeCSVFiles()
    removeInvalidData()
            
    
    
