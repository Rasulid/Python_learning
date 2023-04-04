# number = int(input())
# tmp_original = number
# reversed_number =None
# while tmp_original > 0:
#     (reversed_number * 10)  + (tmp_original % 10 )
#     tmp_original = tmp_original // 10 
#     if number == reversed_number:
#         print('Palindrome')
#     else :
#         print('no palindrome')

# def bmi(weight, height):
#     #your code here
#     bmi = weight / height ** 2
#     if bmi <= 18.5:
#         print('Underweight')
#     elif bmi <= 25.0:
#         print('Normal')
#     elif bmi <= 30.0 :
#         print('Overweight')
#     else :
#         print('Obese')
    
# bmi(81 , 1.85)



# l = [2,3,4,5,6,7,8]
# c = 1
# for x in l :
#     c = x * c
#     print(c)

# def count_sheep(n):
#     result = ''
#     for i in range(1, n + 1):
#         result += str(i) + ' sheep...'
#     print(result)
# count_sheep(3)





# import random
# tries = 0

# number = random.randint(1, 50)

# print('Hmmm... Try to guess what number between 1 and 50 I was thinking about :)')

# while tries < 6:
#     guess = int(input('Take a guess: '))
    
#     tries+=1
    
#     if guess < number:
#         print('Your guess is too low')
        
#     if guess > number:
#         print('Yout guess is too high')
        
#     if guess == number:
#         print(f'Congratulations! You guessed my number in {tries} guesses.')
#         break
        
#     if guess != number and tries == 6:
#         print(f"Sorry, but you didn't make it. My number was: {number}")
#         break

# import random
# continue_s = True

# while continue_s:
#     pleyer_shoose = input('r - камень ,  c -  ножницы ,  p -  бумага = ').lower()


#     if pleyer_shoose not in ['r' , 'c' , 'p']:
#         print('Eror')
#         continue
#     generator = {1:'r',
#                  2:'c',
#                  3:'p'}
#     comp_choose = generator[random.randint(1,3)]
#     # comp_choose = random.choice(['r','s','p'])

#     print(f"Comp choes =  {comp_choose}")

#     win_c = [('p' , 'r'),('r' , 'c'),('c','p')]

#     if comp_choose == pleyer_shoose:
#         print('нечья')

#     elif (pleyer_shoose , comp_choose) in win_c:
#         print('Человек победил!')
    
#     else:
#         print('Компютер победил!')
    
#     continue_s = input('Хотите продолжить ? [y/n] = ').lower() == 'y'





from Konstant import Charecter

s= Charecter(90)
print(s)