class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        
        d = {}

        for name in names:

            if name not in d:
                d[name] = 1
            
            else:
                new_name = name+"("+str(d[name])+")"

                while new_name in d:
                    d[name] += 1
                    new_name = name+"("+str(d[name])+")"
                    # print(d)
                d[new_name] = 1
            
        
        return [k for k,_ in d.items()]

                # val = d[name].findall('.*\((\d+)\)')

                # if val == None:
                #     d[name] = name+"(1)"
                #     d[name+"(1)"] = name+"(1)"
                # else:
                #     d[name] = name + "(" + str(int(val) + 1) + ")"
                #     d[name + "(" + str(int(val) + 1) + ")"] 
