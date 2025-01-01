import pandas as pd
a=[3,5,8]
myvar=pd.Series(a)
print(myvar)

import pandas as pd
a=[1,2,3,4,5,6]
myvar=pd.Series(a,index=["K","A","V","I","Y","A"])
print(myvar)


import pandas as pd
mydata={
    'Food':["Rice","Dosa","Idly"],
    'Price':[100,50,20],
    'Quantity':[2,2,5],
    'Sidedish':["Potato","Sambar","Chutney"],
    
    'Tax':[139,57,28]
}

myvar=pd.DataFrame(mydata)
print(myvar)
                

