import requestdata
from util import showhtml
import sys
# sys.path.append(r"D:\studay")
import getdata
test = requestdata.Requestdata(filename="常用接口文档.xlsx", sheetname="安全保障app")
print(test.filenames)
apidict = test.handle_apidict("数据更新")
print(apidict)
params = [('com.togest.railwayjob', ''), ('com.togest.railwayjob', 2), ('test', ''), ('test', 0.1)]
for i in range(len(params)):
    apidicend_copy = apidict[-1].copy()
    param = apidicend_copy["params"]
    new_params = dict(zip(param.keys(), list(params[i])))
    # print(new_params)
    for key,val in new_params.copy().items():
        if not val:
            new_params.pop(key)
    apidicend_copy["params"] = new_params
    print(apidicend_copy)
    apidictcopy=(apidict[0],apidicend_copy)
    res = test.simple_request(apidictcopy)
    #print(res)
    print(res)

