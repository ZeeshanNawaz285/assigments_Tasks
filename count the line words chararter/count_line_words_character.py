
with open('test.txt' , 'r') as file:
                
        data=file.read()
        
        line_count = len(data)
        lines = data.split('\n')
        line_count = len(lines)
        
        char_count = 0
        word_count = 0
        
        for line in lines:
            char_count += len(line)
            
            line = line.split(' ')
            word_count += len(line)
             
 
               
        print("total number of character are :" , char_count)     
        print("total number of words are : ",word_count)
        print("total number of lines  are : ",line_count)            
