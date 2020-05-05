class SimpleLogisticRegression:
    """
    Simple Logistic Regression using MLE
    """
    def __init__(self, data):
        self.data = data
        self.fit()
    def fit(self):
        

def run():

    data = [ \
        # [AVG #Rooms, AVG $k > 25]
        [6.421, 0], \
        [7.185, 1], \
        [6.998, 1], \
        [7.147, 1], \
        [6.43, 1], \
        [6.012, 0], \
        [6.172, 1], \
        [5.631, 0], \
        [6.004, 0], \
        [6.377, 0], \
        [6.009, 0] \
    ]

    lr = SimpleLogisticRegression(data)
