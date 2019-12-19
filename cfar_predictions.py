def do_predictions(x_test, file_name, model, plt):
    """ assuming test_arr has some cifar data in it
    plot a random sample of the images  and the preidctions
    @param test_arr: sample of cifar images
    @param file_name: name of output image file
    @param model: model trained to classify cifar images
    @param plt: matplotlib plot object
    @return: nothing
    """
    columns = 3
    rows = 2
    img_arr = x_test[np.random.randint(x_test.shape[0], size=(columns*rows))]
    predictions = [get_category(model.predict(img_arr)[i]) for i in range(len(img_arr))]
    fig=plt.figure(figsize=(8, 8))
    for i in range(1, columns*rows +1):
        fig.add_subplot(rows, columns, i)
        plt.imshow(img_arr[i - 1])
        plt.axis('off');
        plt.title(predictions[i - 1])
    fig.savefig(file_name)
    pass
