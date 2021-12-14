


def main():
    
    import pandas as pd
    
    lb = pd.read_csv('linkedbirth.csv')
    data = lb.loc[lb.index[0:],['mracerec','meduc','sex','uprevis','wtgain']]
    data.to_csv('da2.csv')
    
    





if __name__ == '__main__':
    main()
    


    