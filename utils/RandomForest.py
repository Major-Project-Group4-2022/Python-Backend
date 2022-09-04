import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor 
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor



def AQI_calculate(Data):

    data=Data
    DataFrame=pd.read_csv(r'C:\Users\Debasish\Desktop\Project\AQI\utils\MasterData.csv')

    x=DataFrame.drop(['PM25','VM'],axis=1)  # Idependent Variable
    y=DataFrame['PM25']                     # Dependent variable

    x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.3,random_state=31)
    sc=StandardScaler()
    x_train=sc.fit_transform(x_train)
    x_test=sc.fit_transform(x_test)

    # RandomForest

    rf_reg = RandomForestRegressor(n_estimators=150)
    rf_reg.fit(x_train , y_train)
    y_pred=rf_reg.predict(data)


    # KNN

    #knn_reg=KNeighborsRegressor(n_neighbors=10)
    #knn_reg.fit(x_train , y_train)
    #y_pred=knn_reg.predict(data)

    # XGBoost

    #xgb_reg=XGBRegressor(n_estimators=100, reg_lambda=1,gamma=0)
    #xgb_reg.fit(x_train,y_train)
    #y_pred=xgb_reg.predict(data)



    predicted_value=round(y_pred[0],2)

    return predicted_value