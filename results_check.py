def check(matrix,n,last_input,data_dict):
                
                if data_dict[last_input]:
                                for cordinates in data_dict[last_input]:
                                                temp=check_result(matrix,n,cordinates)
                                                if temp==1:
                                                                return 1
                                return 0



def check_result(matrix,n,cordinates):
                x=cordinates[0]
                y=cordinates[1]
#the most tricky part is the cordinate 0 0 because it has three chances to complete the loop
                if x==0 and y==0:
                                if(check_diagonally(matrix,n)==1):
                                                return 1
                                elif(check_col(matrix,y,n)==1):
                                                return 1
                                elif(check_row(matrix,x,n)==1):
                                                return 1
                                else:
                                                return 0
                elif x==0:
                                return check_col(matrix,y,n)
                elif y==0:
                                return check_row(matrix,x,n)
                





def check_diagonally(matrix,n):
                count=1
                for i in range(n-1):
                                if matrix[i][i]==matrix[i+1][i+1]:
                                                count+=1
                                else:
                                                break
                if count==n:
                                return 1
                
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
                                return 1
                if y==n-1:
                                count=1
                                for i in range(n-1):
                                                if matrix[i][y-i]==matrix[i+1][y-i-1]:
                                                                count+=1
                                                else:
                                                                break
                                if count==n:
                                                return 1
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
                                return 1
                if x==n-1:
                                count=1
                                for i in range(n-1):
                                                if matrix[x-i][i]==matrix[x-i-1][i+1]:
                                                                count+=1
                                                else:
                                                                break
                                if count==n:
                                                return 1
                                else:
                                                return 0
