from matplotlib import pyplot as plt

steps = [1,2,3,4,5]

sasc_30min_lstm=[14.69,14.98,15.50,16.12,17.74]
sasc_30min_lstm_cnn=[7.79,7.56,8.14,8.33,9.07]
sasc_30min_svr=[11.02,12.35,12.21,13.96,15.85]
sasc_30min_emd_svr=[15.78,14.31,15.98,17.84,17.62]
sasc_30min_emd_lstm=[9.56,10.14,10.21,11.76,12.32]
sasc_30min_emd_gan=[11.73,11.98,12.09,12.19,12.06]
sasc_30min_our=[9.09,9.34,9.55,9.46,9.71]

sasc_20min_lstm=[13.68,13.99,14.76,15.66,17.04]
sasc_20min_lstm_cnn=[8.55,9.94,11.31,12.22,11.98]
sasc_20min_svr=[11.06,12.31,12.88,13.77,15.01]
sasc_20min_emd_svr=[14.30,14.22,14.76,15.41,15.88]
sasc_20min_emd_lstm=[9.69,9.90,10.34,11.71,13.54]
sasc_20min_emd_gan=[12.20,12.71,12.34,12.56,12.90]
sasc_20min_our=[9.33,9.14,9.56,9.71,9.44]

sasc_10min_lstm=[11.19,11.79,12.41,13.65,15.01]
sasc_10min_lstm_cnn=[8.36,9.41,9.94,10.24,13.41]
sasc_10min_svr=[16.71,15.98,17.65,18.02,20.71]
sasc_10min_emd_svr=[11.20,11,44,12,91,13.04,13.88]
sasc_10min_emd_lstm=[6.62,7.23,8.38,9.96,11.04]
sasc_10min_emd_gan=[9.40,9.56,9.67,9.89,10.02]
sasc_10min_our=[6.58,6.34,6.90,7.81,7.59]

plt.figure(figsize=(12,14))
plt.subplot(311)
plt.plot(steps,sasc_30min_lstm,'.',color='blue',label='LSTM')
plt.plot(steps,sasc_30min_lstm_cnn,color='red',label='LSTM+CNN')
plt.plot(steps,sasc_30min_emd_lstm,'*',color='yellow',label='EMD+LSTM')
plt.plot(steps,sasc_30min_emd_gan,'-.',color='orange',label='EMD+GAN')
plt.plot(steps,sasc_30min_our,'-*',color='black',label='Ours')
plt.subplots_adjust(hspace = 0.45)
plt.title('PWS = 30 Min')
plt.ylabel('MAPE %')
#plt.xlabel('Step Ahead')
plt.grid()
plt.legend(bbox_to_anchor=(0.95, 0.8))

plt.subplot(312)
plt.plot(steps,sasc_20min_lstm,'.',color='blue',label='LSTM')
plt.plot(steps,sasc_20min_lstm_cnn,color='red',label='LSTM+CNN')
plt.plot(steps,sasc_20min_emd_lstm,'*',color='yellow',label='EMD+LSTM')
plt.plot(steps,sasc_20min_emd_gan,'-.',color='orange',label='EMD+GAN')
plt.plot(steps,sasc_20min_our,'-*',color='black',label='Ours')
plt.subplots_adjust(hspace = 0.45)
plt.title('PWS = 20 Min')
plt.ylabel('MAPE %')
#plt.xlabel('Step Ahead')
plt.grid()
plt.legend(bbox_to_anchor=(0.95, 0.8))

plt.subplot(313)
plt.plot(steps,sasc_10min_lstm,'.',color='blue',label='LSTM')
plt.plot(steps,sasc_10min_lstm_cnn,color='red',label='LSTM+CNN')
plt.plot(steps,sasc_10min_emd_lstm,'*',color='yellow',label='EMD+LSTM')
plt.plot(steps,sasc_10min_emd_gan,'-.',color='orange',label='EMD+GAN')
plt.plot(steps,sasc_10min_our,'-*',color='black',label='Ours')
plt.title('PWS = 10 Min')
plt.ylabel('MAPE %')
plt.xlabel('Forcasting Steps Ahead')
plt.grid()
plt.legend(bbox_to_anchor=(0.95, 0.8))

plt.savefig("sasc-steps-cmp.png")
plt.show()