#Gale-shapley Algorithm     O(n^2)

#Initialising with men and women with preferences
m = [{ 
  "name":"m1",
  "preferences": ["w2","w4","w1","w3","w5"]  ,
  "status":"False",
  "partner":"none",
  "forbidden":"w4"
    },
    { 
  "name":"m2",
  "preferences": ["w5","w3","w1","w5","w4"]  ,
  "status":"False",
  "partner":"none",
  "forbidden":""
    },
    { 
  "name":"m3",
  "preferences": ["w1","w5","w4","w2","w3"]  ,
  "status":"False",
  "partner":"none",
  "forbidden":"w2"
    },
    { 
  "name":"m4",
  "preferences": ["w1","w5","w2","w3","w4"]  ,
  "status":"False",
  "partner":"none",
  "forbidden":"w1"
    },
    { 
  "name":"m5",
  "preferences": ["w3","w2","w5","w4","w1"]  ,
  "status":"False",
  "partner":"none",
  "forbidden":["w2","w3","w4"]
    }
] 

w = [{ 
  "name":"w1",
  "preferences": ["m2","m4","m1","m5","m3"]  ,
  "status":"False",
  "partner":"none"
    },
    { 
  "name":"w2",
  "preferences": ["m5","m4","m1","m3","m2"] ,
  "status":"False",
  "partner":"none"
    },
    { 
  "name":"w3",
  "preferences": ["m1","m5","m4","m2","m3"]  ,
  "status":"False",
  "partner":"none"
    },
    { 
  "name":"w4",
  "preferences": ["m3","m2","m5","m4","m1"]  ,
  "status":"False",
  "partner":"none"
    },
    { 
  "name":"w5",
  "preferences": ["m4","m5","m2","m3","m1"],
  "status":"False",
  "partner":"none"
    }
]


pairs = []

def find(x):
    for woman in w:
        if woman["name"] == x:     
            return woman
        else: 
            for man in m:    
                if man["name"] == x:
                    return man
                else:
                    pass            

def pair(x,y):
    pair = [x["name"],y["name"]]
    x["status"] = "True"
    y["status"] = "True"
    x["partner"] = y["name"]
    y["partner"] = x["name"] 
    print("congrats")
    print(pair)
    pairs.append(pair)

def findprefer(x,subject,aukad):
    current = find(subject["partner"])
    print("intrested in" , subject["name"])
    print("current partner",current["name"])
    xpref   = subject["preferences"].index(x["name"])
    print("prefer at ", xpref)
    if xpref < subject["preferences"].index(current["name"]):
        print("stole") 
        pair(x,subject)
        current["status"] = "False"
        current["partner"] = "none"
    else:
        print("unchanged")
        aukad = aukad+1
        return aukad
        pass

#Algorihtm

for guy in m:
    aukad=0 
    while guy["status"] == "False":
        print(guy["name"])
        print("------------")
        woman = find(guy["preferences"][aukad])
        if woman["name"] in guy["forbidden"]:
            aukad= aukad+1
            print('forbidden with',woman["name"])
            continue
        if woman["status"] == "False":
            pair(guy,woman)
            guy["status"] = "True"
            woman["status"] ="True"
        else:
            aukad = findprefer(guy,woman,aukad)
            print("aukad ",aukad)
            pass
        print("   ")
print("pairs formed -  ",pairs)


#! Note

# Returned set S is always a stable matching 
# m's proposals gets worse while w's matches gets better
# in case of independent sets as in forbidden pairs line 112 will change to   
#   woman = find(guy["preferences"][aukad])
#   if woman["name"] in guy["forbidden"]:
#        aukad= aukad+1
