#!/usr/bin/env python
# coding: utf-8

# # Bài tập lập trình 5: break RSA  
# *Nguyễn Hồng Đăng 20160988*

# In[1]:


#!/usr/bin/env python3
import gmpy2
from gmpy2 import mpz


# ## Question 1:

# In[2]:


print('\nQuestion 1:')
n1=mpz('17976931348623159077293051907890247336179769789423065727343008115 77326758055056206869853794492129829595855013875371640157101398586 47833778606925583497541085196591615128057575940752635007475935288 71082364994994077189561705436114947486504671101510156394068052754 0071584560878577663743040086340742855278549092581')


# Tính x theo gợi ý

# In[3]:


a=gmpy2.isqrt(n1)+1
temp=gmpy2.sub(gmpy2.mul(a,a),n1)
x,remain=gmpy2.isqrt_rem(temp)
print(x,remain,sep='\t')


# ### Kết quả:

# In[4]:


p=gmpy2.sub(a,x)
q=gmpy2.add(a,x)
print('p is:',p,sep='\n')


# Lưu giá trị p,q cho question 3

# In[5]:


q3_factorization=(p,q)


# ## Question 2:

# In[6]:


print('\nQuestion 2:')
n2=mpz('6484558428080716696628242653467722787263437207069762630604390703787 9730861808111646271401527606141756919558732184025452065542490671989 2428844841839353281972988531310511738648965962582821502504990264452 1008852816733037111422964210278402893076574586452336833570778346897 15838646088239640236866252211790085787877')


# Lặp cho tới khi tìm được x thỏa mãn

# In[7]:


for i in range(1,2**20):
    a=gmpy2.isqrt(n2)+i
    temp=gmpy2.sub(gmpy2.mul(a,a),n2)
    x,remain=gmpy2.isqrt_rem(temp)
    if remain==0:
        break
p=gmpy2.sub(a,x)
q=gmpy2.add(a,x)


# ### Kết quả:

# In[8]:


print('Sucessfully after iterations number',i)
print('p is:',p,sep='\n')


# ## Question 3:

# In[9]:


print('\nQuestion 3:')
n3=mpz('72006226374735042527956443552558373833808445147399984182665305798191 63556901883377904234086641876639384851752649940178970835240791356868 77441155132015188279331812309091996246361896836573643119174094961348 52463970788523879939683923036467667022162701835329944324119217381272 9276147530748597302192751375739387929')


# Đặt A=3p+2q và x=3p-2q  
# #### Nhận xét:
# - Chứng minh tương tự gợi ý, ta được A=2* ceil(sqrt(6*N))+1. Từ đó tính được A
# - (A+x)(A-x)=24pq=24N nên |x|=sqrt(A^2-24N). Từ đó tính được |x|
# Từ A và x, tính được p và q. Cần chú ý rằng x có thể âm.
# ### Kết quả:

# In[10]:


a=2*gmpy2.isqrt(6*n3)+1
temp=gmpy2.sub(gmpy2.mul(a,a),24*n3)
x,remain=gmpy2.isqrt_rem(temp)
print(x,remain,sep='\t')
p,r=gmpy2.t_divmod(gmpy2.add(a,x),6)
if r!=0:
    print('3p-2q is negative')
    p,r=gmpy2.t_divmod(gmpy2.sub(a,x),6)
    print(r)
print('p is:',p,sep='\n')


# ## Question 4:

# In[11]:


print('\nQuestion 4:')
cipher=mpz('22096451867410381776306561134883418017410069787892831071731839143676135600120 53800428232965047350942434394621975151225646583996794288946076454204058156474 89880137348641204523252293201764879166664029975091887299716905260832220677716 00019329260870009579993724077458967773697817571267229951148662959627934791540')


# RSA sử dụng modulus N ở question 1, Encryption exponent e=65537

# In[12]:


p,q=q3_factorization
e=mpz('65537')
fi=gmpy2.mul(p-1,q-1)


# Tìm (g,d,t) thỏa mãn e*d=1 (mod fi), hay g=e*d+fi* t (Trong đó g=1)

# In[13]:


g,d,t=gmpy2.gcdext(e,fi)
print(g,d,sep='\n')


# RSA Decryption sử dụng d tìm được ở trên

# In[14]:


plain=gmpy2.powmod(cipher,d,n1)
#2 bytes đầu chứa thông tin của mpz object, lọai bỏ
plain_hex=bytearray(gmpy2.to_binary(plain)[2:])
print(plain_hex)


# Sửa lại thứ tự các bytes
# ### Kết quả:

# In[15]:


plain_hex.reverse()
print(plain_hex)


# **Kết quả là:**  
# *"Factoring lets us break RSA."*
