def check(matrix,n,last_input,data_dict):
                
                if data_dict[last_input]:
                                for cordinates in data_dict[last_input]:
                                                temp=check_result(matrix,n,cordinates)
                                                
                                                if temp:
                                                                return temp
                                return 0



def check_result(matrix,n,cordinates):
                x=cordinates[0]#getting x
                y=cordinates[1]#getting y
#the most tricky part is the cordinate 0 0 because it has three chances to complete the loop
                if x==0 and y==0:
                                temp=check_diagonally(matrix,n)
                                if(temp):
                                                return temp
                                temp=check_col(matrix,y,n)
                                if(temp):
                                                return temp
                                temp=check_row(matrix,x,n)
                                if temp:
                                                return temp
                                else:
                                                return 0
                elif x==0:
                                temp= check_col(matrix,y,n)
                                if temp:
                                                return temp
                elif y==0:
                                temp=check_row(matrix,x,n)
                                if temp:
                                                return temp
                





def check_diagonally(matrix,n):
                
                count=1
                for i in range(n-1):
                                if matrix[i][i]==matrix[i+1][i+1]:
                                                count+=1
                                else:
                                                break
                if count==n:
                                temp=[1,n*n]
                                
                                return temp
                
                else:
                                return 0




def check_col(matrix,y,n):
                
                count=1
                for i in range(n-1):
                                if matrix[i][y]==matrix[i+1][y]:
                                                count+=1
                                else:
                                                break
                if count==n:
                                temp=[y+1,(n-1)*n+y+1]
                                
                                return temp
                if y==n-1:
                                count=1
                                for i in range(n-1):
                                                if matrix[i][y-i]==matrix[i+1][y-i-1]:
                                                                count+=1
                                                else:
                                                                break
                                if count==n:
                                                temp=[y+1,n*(n-1)+1]
                                                
                                                return temp
                                else:
                                                return 0




def check_row(matrix,x,n):
                count=1
                for i in range(n-1):
                                if matrix[x][i]==matrix[x][i+1]:
                                                count+=1
                                else:
                                                break
                
                if count==n:
                                temp=[x*n+1,(x+1)*n]
                                return [x*n+1,(x+1)*n]
                elif x==n-1:
                                count=1
                                for i in range(n-1):
                                                if matrix[x-i][i]==matrix[x-i-1][i+1]:
                                                                count+=1
                                                else:
                                                                break
                                if count==n:
                                                temp=[x*n+1,n]
                                                
                                                return temp
                                else:
                                                return 0
