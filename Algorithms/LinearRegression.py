class SimpleLinearRegression:
    """
    Simple Linear Regression using OLS
    """
    def __init__(self, data):
        self.data = data
        self.fit()
    def fit(self):
        X = [x[0] for x in self.data]
        y = [x[1] for x in self.data]
        # Averages
        y_hat = sum(y)/len(y)
        x_hat = sum(X)/len(X)
        # OLS to estimate coefficients
        self.beta_1_hat = sum([((X[i] - x_hat) * (y[i] - y_hat)) for i in range(0, len(X))]) / sum([(x - x_hat)**2 for x in X])
        self.beta_0_hat = y_hat - (self.beta_1_hat * x_hat)
        print("fit complete")
        print("y = " + str(self.beta_0_hat)+" + " + str(self.beta_1_hat) + "*X")
        return True

def run():

    data = [ \
        # [AVG #Rooms, AVG $k]
        [6.421, 21.6], \
        [7.185, 34.7], \
        [6.998, 33.4], \
        [7.147, 36.2], \
        [6.43, 28.7], \
        [6.012, 22.9], \
        [6.172, 27.1], \
        [5.631, 16.5], \
        [6.004, 18.9], \
        [6.377, 15], \
        [6.009, 18.9] \
    ]

    lr = SimpleLinearRegression(data)
