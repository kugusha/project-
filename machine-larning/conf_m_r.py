import matplotlib.pyplot as plt

def plot_confusion_matrix(cm, class, cmap=plt.cm.Blues):

    title='Confusion matrix'

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()


    tick_marks = np.arange(len(class))
    plt.xticks(tick_marks, class, rotation=45)
    plt.yticks(tick_marks, class)
    plt.tight_layout()
    plt.ylabel('True')
    plt.xlabel('Predicted')
    

"""def class_report(fig, cr, classes, size, with_avg_total=True, cmap=plt.cm.autumn):
    lines = filter(None, cr.split("\n"))
    
    columns = lines[0].split()[:-1]
    data_matrix = []
        
    # Get data for every class, without average
    for line in lines[1:-1]:
        line = line.split()[1:-1]
        data_matrix.append(map(float, line))
        
    # Get average list
    average_line = lines[-1].split()[3:-1]
    data_matrix.append(map(float, average_line))
    
    # Plotting
    ax = fig.add_subplot(size)
    h = ax.matshow(data_matrix, cmap = cmap)
    fig.colorbar(h)
    ax.set_xticklabels([''] + columns, fontsize = 25, rotation = 45)
    ax.set_yticklabels([''] + classes + ['Average'], fontsize = 25)
    
    ax.set_xlabel('Metrics', fontsize = 40)
    ax.set_ylabel('Classes', fontsize = 40)

#     print "Classes: ", classes
#     print "Data matrix: ", data_matrix
    
    # Add test to squares

    for y in range(len(classes) + 1):
        for x in range(len(data_matrix[0])):
            ax.text(x, y, data_matrix[y][x], fontsize = 20, va='center', ha='center') """