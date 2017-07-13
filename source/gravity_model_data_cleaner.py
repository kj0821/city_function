import math, csv

def Euclidean_Distance(data1, data2):
    
    #print data1, data2
    
    return round(math.sqrt(sum([pow(float(data1[i]) - float(data2[i]),2) for i in range(len(data1))])),3)

def getFunctionData(path):
    
    dataDict = {}
    
    with open(path) as f:
        reader = csv.reader(f)        
        headers = next(reader)[1:]

        for row in reader:
            dong = row[0]
            dong = dong.replace(",",".")
            
            data = row[1:]
            
            dataDict[dong] = data
    
    return dataDict        

def functional_distance():
    dongList = ["Sajik-dong","Samcheong-dong","Buam-dong","Pyeongchang-dong","Muak-dong","Gyonam-dong","Gahoe-dong","Jongno 1.2.3.4-ga-dong","Jongno 5.6-ga-dong","Ihwa-dong","Changsin 1-dong","Changsin 2-dong","Changsin 3-dong","Sungin 1-dong","Sungin 2-dong","Cheongunhyoja-dong","Hyehwa-dong","Sogong-dong","Hoehyeon-dong","Myeong-dong","Pil-dong","Jangchung-dong","Gwanghui-dong","Euljiro-dong","Sindang 1-dong","Sindang 2-dong","Sindang 3-dong","Sindang 4-dong","Sindang 5-dong","Sindang 6-dong","Hwanghak-dong","Jungnim-dong","Huam-dong","Yongsan 2-ga-dong","Namyeong-dong","Wonhyoro 2-dong","Hyochang-dong","Yongmun-dong","Ichon 1-dong","Ichon 2-dong","Itaewon 1-dong","Itaewon 2-dong","Seobinggo-dong","Bogwang-dong","Cheongpa-dong","Wonhyoro 1-dong","Hangangro-dong","Hannam-dong","Wangsimni 2-dong","Majang-dong","Sageun-dong","Haengdang 1-dong","Haengdang 2-dong","Eungbong-dong","Geumho 1-ga-dong","Geumho 4-ga-dong","Seongsu 1-ga1-dong","Seongsu 1-ga2-dong","Seongsu 2-ga1-dong","Seongsu 2-ga 3-dong","Songjeong-dong","Yongdap-dong","Wangsimridoseon-dong","Geumho 2.3ga-dong","Oksu-dong","Hwayang-dong","Gunja-dong","Junggok 1-dong","Junggok 2-dong","Junggok 3-dong","Junggok 4-dong","Neung-dong","Guui 1-dong","Guui 2-dong","Guui 3-dong","Gwangjang-dong","Jayang 1-dong","Jayang 2-dong","Jayang 3-dong","Jayang 4-dong","Hoegi-dong","Hwigyeong 1-dong","Hwigyeong 2-dong","Cheongryangri-dong","Yongsin-dong","Jegi-dong","Jeollo 1-dong","Jeollo 2-dong","Dapsimri 1-dong","Dapsimri 2-dong","Jangan 1-dong","Jangan 2-dong","Imun 1-dong","Imun 2-dong","Myeonmok 2-dong","Myeonmok 4-dong","Myeonmok 5-dong","Myeonmok 7-dong","Sangbong 1-dong","Sangbong 2-dong","Junghwa 1-dong","Junghwa 2-dong","Muk 1-dong","Muk 2-dong","Mangu 3-dong","Sinnae 1-dong","Sinnae 2-dong","Myeonmokbon-dong","Myeonmok 3.8-dong","Mangubon-dong","Donam 1-dong","Donam 2-dong","Anam-dong","Bomun-dong","Jeongneung 1-dong","Jeongneung 2-dong","Jeongneung 3-dong","Jeongneung 4-dong","Gireum 1-dong","Gireum 2-dong","Wolgok 1-dong","Wolgok 2-dong","Jangwi 1-dong","Jangwi 2-dong","Jangwi 3-dong","Seongbuk-dong","Samseon-dong","Dongseon-dong","Jongam-dong","Seokgwan-dong","Beon 1-dong","Beon 2-dong","Beon 3-dong","Suyu 1-dong","Suyu 2-dong","Suyu 3-dong","Samyang-dong","Mia-dong","Songjung-dong","Songcheon-dong","Samgaksan-dong","Ui-dong","Insu-dong","Ssangmun 1-dong","Ssangmun 2-dong","Ssangmun 3-dong","Ssangmun 4-dong","Banghak 1-dong","Banghak 2-dong","Banghak 3-dong","Chang 1-dong","Chang 2-dong","Chang 3-dong","Chang 4-dong","Chang 5-dong","Dobong 1-dong","Dobong 2-dong","Wolgye 1-dong","Wolgye 2-dong","Wolgye 3-dong","Gongneung 2-dong","Hagye 1-dong","Hagye 2-dong","Junggyebon-dong","Junggye 1-dong","Junggye 4-dong","Sanggye 1-dong","Sanggye 2-dong","Sanggye 5-dong","Sanggye 8-dong","Sanggye 9-dong","Sanggye 10-dong","Gongneung 1.3-dong","Sanggye 3.4-dong","Sanggye 6.7-dong","Junggye 2.3-dong","Nokbeon-dong","Bulgwang 1-dong","Galhyeon 1-dong","Galhyeon 2-dong","Gusan-dong","Daejo-dong","Eungam 1-dong","Eungam 2-dong","Sinsa 1-dong","Sinsa 2-dong","Jeungsan-dong","Susaek-dong","Jingwan-dong","Bulgwang-dong","Eungam 3-dong","Yeokchon-dong","Cheonyeon-dong","Hongje 1-dong","Hongje 3-dong","Hongje 2-dong","Hongeun 1-dong","Hongeun 2-dong","Namgajwa 1-dong","Namgajwa 2-dong","Bukgajwa 1-dong","Bukgajwa 2-dong","Chunghyeon-dong","Bukahyeon-dong","Sinchon-dong","Yeonhui-dong","Yonggang-dong","Daeheung-dong","Yeomni-dong","Sinsu-dong","Seogyo-dong","Hapjeong-dong","Mangwon 1-dong","Mangwon 2-dong","Yeonnam-dong","Seongsan 1-dong","Seongsan 2-dong","Sangam-dong","Dohwa-dong","Seogang-dong","Gongdeok-dong","Ahyeon-dong","Mok 1-dong","Mok 2-dong","Mok 3-dong","Mok 4-dong","Sinwol 1-dong","Sinwol 2-dong","Sinwol 3-dong","Sinwol 4-dong","Sinwol 5-dong","Sinwol 6-dong","Sinwol 7-dong","Sinjeong 1-dong","Sinjeong 2-dong","Sinjeong 3-dong","Sinjeong 6-dong","Sinjeong 7-dong","Mok 5-dong","Sinjeong 4-dong","Yeomchang-dong","Deungchon 1-dong","Deungchon 2-dong","Deungchon 3-dong","Hwagokbon-dong","Hwagok 2-dong","Hwagok 3-dong","Hwagok 4-dong","Hwagok 6-dong","Hwagok 8-dong","Gayang 1-dong","Gayang 2-dong","Gayang 3-dong","Balsan 1-dong","Gonghang-dong","Banghwa 1-dong","Banghwa 2-dong","Banghwa 3-dong","Hwagok 1-dong","Ujangsan-dong","Sindorim-dong","Guro 1-dong","Guro 3-dong","Guro 4-dong","Guro 5-dong","Gocheok 1-dong","Gocheok 2-dong","Gaebong 2-dong","Gaebong 3-dong","Oryu 1-dong","Oryu 2-dong","Sugung-dong","Garibong-dong","Guro 2-dong","Gaebong 1-dong","Gasan-dong","Doksan 1-dong","Doksan 2-dong","Doksan 3-dong","Doksan 4-dong","Siheung 1-dong","Siheung 2-dong","Siheung 3-dong","Siheung 4-dong","Siheung 5-dong","Yeouido-dong","Dangsan 1-dong","Dangsan  2-dong","Yangpyeong 1-dong","Yangpyeong 2-dong","Singil 1-dong","Singil 3-dong","Singil 4-dong","Singil 5-dong","Singil 6-dong","Singil 7-dong","Daerim 1-dong","Daerim 2-dong","Daerim 3-dong","Yeongdeungpo bon-dong","Yeongdeungpo-dong","Dorim-dong","Mullae-dong","Noryangjin 2-dong","Sangdo 1-dong","Sangdo 2-dong","Sangdo 3-dong","Sangdo 4-dong","Sadang 1-dong","Sadang 3-dong","Sadang 4-dong","Sadang 5-dong","Daebang-dong","Sindaebang 1-dong","Sindaebang 2-dong","Heukseok-dong","Noryangjin 1-dong","Sadang-dong","Boramae-dong","Cheongnim-dong","Haengun-dong","Nagseongdae-dong","Jungang-dong","Inheon-dong","Namhyeon-dong","Sewon-dong","Sinwon-dong","Serim-dong","Gwanak-gu Sinsa-dong","Sillim-dong","Nanhyang-dong","Jowon-dong","Daehak-dong","Euncheon-dong","Seonghyeon-dong","Chengnyong-dong","Nangok-dong","Samseong-dong","Miseong-dong","Seocho 1-dong","Seocho 2-dong","Seocho 3-dong","Seocho 4-dong","Jamwon-dong","Banpobon-dong","Banpo 1-dong","Banpo 2-dong","Banpo 3-dong","Banpo 4-dong","Bangbaebon-dong","Bangbae 1-dong","Bangbae 2-dong","Bangbae 3-dong","Bangbae 4-dong","Yangjae 1-dong","Yangjae 2-dong","Naegok-dong","Gannam-gu Sinsa-dong","Nonhyeon 1-dong","Nonhyeon 2-dong","Samseong 1-dong","Samseong 2-dong","Daechi 1-dong","Daechi 4-dong","Yeoksam 1-dong","Yeoksam 2-dong","Dogok 1-dong","Dogok 2-dong","Gaepo 1-dong","Gaepo 4-dong","Irwonbon-dong","Irwon 1-dong","Irwon 2-dong","Suseo-dong","Segok-dong","Apgujeong-dong","Cheongdam-dong","Daechi 2-dong","Gaepo 2-dong","Pungnap 1-dong","Pungnap 2-dong","Geoyeo 1-dong","Geoyeo 2-dong","Macheon 1-dong","Macheon 2-dong","Bangi 1-dong","Bangi 2-dong","Oryun-dong","Ogeum-dong","Songpa 1-dong","Songpa 2-dong","Seokchon-dong","Samjeon-dong","Garakbon-dong","Garak 1-dong","Garak 2-dong","Munjeong 1-dong","Munjeong 2-dong","Jangji-dong","Jamsilbon-dong","Jamsil 4-dong","Jamsil 6-dong","Jamsil 7-dong","Jamsil 2-dong","Jamsil 3-dong","Gangil-dong","Sangil-dong","Myeongil 1-dong","Myeongil 2-dong","Godeok 1-dong","Godeok 2-dong","Amsa 2-dong","Amsa 3-dong","Cheonho 1-dong","Cheonho 3-dong","Seongnae 1-dong","Seongnae 2-dong","Seongnae 3-dong","Dunchon 1-dong","Dunchon 2-dong","Amsa 1-dong","Cheonho 2-dong","Gil-dong"]
    dataDict1 = getFunctionData("../data/dong_data/function1_data.csv")
    dataDict2 = getFunctionData("../data/dong_data/function2_data.csv")
            
    with open("../data/dong_data/functional_distance.csv","w") as fw:
        fw.write("origin,destination,fd1,fd2\n")
        for dong1 in dongList:
            print(dong1)
            for dong2 in dongList:
                if dong1 != dong2:
                    fd1 = Euclidean_Distance(dataDict1[dong1], dataDict1[dong2])
                    fd2 = Euclidean_Distance(dataDict2[dong1], dataDict2[dong2])                    
                    fw.write("%s,%s,%s,%s\n" % (dong1, dong2, fd1, fd2))
                #print dong1, dong2, Euclidean_Distance(dataDict[dong1], dataDict[dong2])

def getMassDict():
    massDict = {}
    
    with open("../data/dong_data/dong_mass.csv") as f:
        reader = csv.DictReader(f)
                
        for row in reader:
            massDict[row['dong']] = row
    
    return massDict

def getDistanceDict():
    distanceDict = {}
    
    with open("../data/dong_data/dong_distance.csv") as f:
        reader = csv.reader(f)
        
        count = 0
        for row in reader:
            if count == 0:
                count += 1
                continue
            
            
            row[0] = row[0].replace(",",".")
            row[1] = row[1].replace(",",".")
            
            
            key = tuple(sorted(row[0:2]))
            distanceDict[key] = float(row[2]) * 1000
    
    return distanceDict

def getTrafficDict():
    trafficDict = {}
    
    with open("../data/dong_data/dong_traffic.csv") as f:
        reader = csv.reader(f)
        
        count = 0
        for row in reader:
            if count == 0:
                count += 1
                continue
            
            row[0] = row[0].replace(",",".")
            row[1] = row[1].replace(",",".")
            
            
            key = tuple(row[0:2])
            
            trafficDict[key] = int(row[2])

         
    return trafficDict

def mergeData():
    
    massDict = getMassDict()    
    distanceDict = getDistanceDict()    
    trafficDict = getTrafficDict()    
     
    
    writeList = []
    
    with open("../data/dong_data/functional_distance.csv") as f:
        reader = csv.DictReader(f)
        
        count = 0
        
        
        for row in reader:        
            count += 1
            key = (row['origin'], row['destination'])
            dkey = tuple(sorted(key))
            
            
            row['distance'] = distanceDict[dkey]
            
            
            try:
                row['traffic'] = trafficDict[key]
            except:
                row['traffic'] = 0
            
            for key in massDict[row['origin']].keys():
                row['origin_%s' % key] = massDict[row['origin']][key]
            
            for key in massDict[row['destination']].keys():
                row['destination_%s' % key] = massDict[row['destination']][key]    
            
            row.pop("origin")
            row.pop("destination")
            
            writeList.append(row)
            
            if count % 10000 == 0: print(count)

        
    with open("../output/gravity_model_data.csv","w", newline="\n") as fw:
        fieldnames = writeList[0].keys()
        writer = csv.DictWriter(fw, fieldnames = fieldnames)
    
        writer.writeheader()
        
        for row in writeList:
            writer.writerow(row)
            
            
if __name__ == '__main__':                
    functional_distance()
    mergeData()
    