import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
'''
step=[]
reward=[]

for i in range(1):
    step.append(np.load(str(i)+'step_smcv_mp.npy'))
    reward.append(np.load(str(i)+'reward_smcv_mp.npy'))
    print(str(i)+':'+str(len(step[i])))
step=np.array(step)
reward=np.array(reward)
'''
x=np.array(range(0,400))
dmpsh05step=np.load('adam_step_dmpshare_w05.npy')
dmpsh05reward=np.load('adam_reward_dmpshare_w05.npy')
dmpsep05step=np.load('adam_step_dmpsep_w05.npy')
dmpsep05reward=np.load('adam_reward_dmpsep_w05.npy')
dmpsep01step=np.load('adam_step_dmpsep_w01.npy')
dmpsep01reward=np.load('adam_reward_dmpsep_w01.npy')
dqnstep=np.load('adam_step_dqn1.npy')
dqnreward=np.load('adam_reward_dqn1.npy')

print(dmpsh05step.shape)
print(dmpsep05step.shape)
print(dmpsep01step.shape)
print(dqnstep.shape)

plt.fill_between(x,np.mean(dqnstep,axis=0)-np.std(dqnstep,axis=0),np.mean(dqnstep,axis=0)+np.std(dqnstep,axis=0),alpha=0.1,color='b')
plt.plot(np.mean(dqnstep,axis=0),'b',label='dqn')
plt.fill_between(x,np.mean(dmpsep05step,axis=0)-np.std(dmpsep05step,axis=0),np.mean(dmpsep05step,axis=0)+np.std(dmpsep05step,axis=0),alpha=0.1,color='r')
plt.plot(np.mean(dmpsep05step,axis=0),'r',label='dmpsep w0.5')
plt.fill_between(x,np.mean(dmpsep01step,axis=0)-np.std(dmpsep01step,axis=0),np.mean(dmpsep01step,axis=0)+np.std(dmpsep01step,axis=0),alpha=0.1,color='g')
plt.plot(np.mean(dmpsep01step,axis=0),'g',label='dmpsep w0.1')
plt.fill_between(x,np.mean(dmpsh05step,axis=0)-np.std(dmpsh05step,axis=0),np.mean(dmpsh05step,axis=0)+np.std(dmpsh05step,axis=0),alpha=0.1,color='y')
plt.plot(np.mean(dmpsh05step,axis=0),'y',label='dmpshare w0.5')
plt.legend(loc='upper left')
plt.savefig('stepcomp.png')
plt.clf()

plt.fill_between(x,np.mean(dqnreward,axis=0)-np.std(dqnreward,axis=0),np.mean(dqnreward,axis=0)+np.std(dqnreward,axis=0),alpha=0.1,color='b')
plt.plot(np.mean(dqnreward,axis=0),'b',label='dqn')
plt.fill_between(x,np.mean(dmpsep05reward,axis=0)-np.std(dmpsep05reward,axis=0),np.mean(dmpsep05reward,axis=0)+np.std(dmpsep05reward,axis=0),alpha=0.1,color='r')
plt.plot(np.mean(dmpsep05reward,axis=0),'r',label='dmpsep w0.5')
plt.fill_between(x,np.mean(dmpsep01reward,axis=0)-np.std(dmpsep01reward,axis=0),np.mean(dmpsep01reward,axis=0)+np.std(dmpsep01reward,axis=0),alpha=0.1,color='g')
plt.plot(np.mean(dmpsep01reward,axis=0),'g',label='dmpsep w0.1')
plt.fill_between(x,np.mean(dmpsh05reward,axis=0)-np.std(dmpsh05reward,axis=0),np.mean(dmpsh05reward,axis=0)+np.std(dmpsh05reward,axis=0),alpha=0.1,color='y')
plt.plot(np.mean(dmpsh05reward,axis=0),'y',label='dmpshare w0.5')
plt.legend(loc='upper left')
plt.savefig('rewardcomp.png')
'''
plt.fill_between(x,np.mean(reward,axis=0)-np.std(reward,axis=0),np.mean(reward,axis=0)+np.std(reward,axis=0),alpha=0.1,color='r')
plt.plot(np.mean(reward,axis=0),'r',label='reward')
plt.legend(loc='upper left')
plt.savefig('st.png')
'''
