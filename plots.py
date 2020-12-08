import numpy as np
import matplotlib.pyplot as plt

def plot_train_val(m_train, m_val, period=25, al_param=False, metric='IoU'):
    
    plt.title('Evolution of the '+metric+ ' with respect to the number of epochs',fontsize=14)
    
    
    if al_param:
        al_steps = np.array(  range( 1, int(len(m_train)*period/al_param +1) )  ) *al_param
        for al_step in al_steps:
            plt.axvline(al_step, color='black')
    plt.plot(np.array(range(1,len(m_train)+1))*period, m_train, color='blue', marker='o', ls=':', label=metric+' train')
    plt.plot(np.array(range(1,len(m_val)+1))*period, m_val, color='red', marker='o', ls=':', label=metric+' val')
    

    plt.xlabel('Number of Epochs')
    plt.ylabel(metric)
    plt.legend(loc = 'upper right')
    plt.savefig('evol_'+metric)
    plt.show()
    