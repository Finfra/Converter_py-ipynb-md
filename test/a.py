# # 1. 아주 간단한 버전의 MLP
# ## library
# 최소한으로 필요한 라이브러리들 선언
# In[ ]:


import numpy as np
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# ## 데이터 셋 불러오기
# iris 데이터셋을 활용할 예정
# In[ ]:


from sklearn import datasets
iris = datasets.load_iris()
x=iris.data
y = keras.utils.to_categorical(iris.target, 3)


# ## 모델 구성
# 간단하게 모델 구성하기
# In[ ]:


model = Sequential()
model.add(Dense(4, activation='relu', input_shape=(4,)))
model.add(Dense(3, activation='softmax'))
model.summary()


# 사용할 fuction 들을 지정
# In[ ]:


model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])


# ## 모델 학습 및 테스트 결과 보기
# fit을 통해 학습을 하고 score 확인
# In[ ]:


model.fit(x, y,
          batch_size=10,
          epochs=100,
          verbose=0
)




score = model.evaluate(x, y, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])


# ## 적용 예
# 실제로 다른 꽃을 측정하여 모델에 집어 넣어 이 꽃이 어떤 것인지 알고자 할 경우
# In[ ]:


x[:1,:],y[:1,:],x[60:61,:],y[60:61,:]



# In[ ]:


x_test=np.array( [ [5.1, 3.5, 1.4, 0.2],[5. , 2. , 3.5, 1. ]])
r=model.predict(x_test)
np.argmax(r, axis=-1)


# # 위와 같이 나오는 0,1,2 의 값은 우리가 원하는 답이 아님(Decoding이 되어 있지 않음.)
