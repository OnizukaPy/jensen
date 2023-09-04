# importera bibliotek
from matplotlib import pyplot as plt

# funktion för att plotta förvirringsmatrisen
def print_history(history, val=False):
        acc = list(history.history.keys())[1]
        
        loss = list(history.history.keys())[0]
        

        if val==False:
                plt.figure(figsize=(12, 6), facecolor='white')

                plt.subplot(1, 2, 1)
                plt.plot(history.history[loss], label='loss')
                plt.xlabel('epoch')
                plt.ylabel('loss')
                plt.title('loss')
                plt.legend()

                plt.subplot(1, 2, 2)
                plt.plot(history.history[acc], label='accuracy')
                plt.xlabel('epoch')
                plt.ylabel('accuracy')
                plt.title('accuracy')
                plt.legend()
        else:
                val_acc = list(history.history.keys())[3]
                val_loss = list(history.history.keys())[2]
                plt.subplot(1,2,1)
                plt.plot(history.history[loss], label='Training loss')
                plt.plot(history.history[val_loss], label='Validation loss')
                plt.title('Training and validation loss')
                plt.xlabel('Epochs')
                plt.ylabel('Loss')
                plt.legend()

                plt.subplot(1,2,2)
                plt.plot(history.history[acc], label='Training accuracy')
                plt.plot(history.history[val_acc], label='Validation accuracy')
                plt.title('Training and validation accuracy')
                plt.xlabel('Epochs')
                plt.ylabel('Accuracy')
                plt.legend()

        plt.tight_layout()
        plt.show()