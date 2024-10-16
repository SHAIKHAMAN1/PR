import numpy as np

# Mean vectors and covariance matrices for Class A and Class B
mean_class_A = np.array([2, 3])  # Mean vector for Class A
cov_class_A = np.array([[1, 0.5], [0.5, 1]])
mean_class_B = np.array([5, 6])  # Mean vector for Class B
cov_class_B = np.array([[1, -0.5], [-0.5, 1]])

def discriminant_function(feature_vector, mean, covariance_matrix):
    inverse_covariance_matrix = np.linalg.inv(covariance_matrix)
    diff = feature_vector - mean
    exponent = -0.5 * np.dot(np.dot(diff, inverse_covariance_matrix), diff.T)
    discriminant_value = exponent - 0.5 * np.log(np.linalg.det(covariance_matrix))
    return discriminant_value

# Function to classify the object into Class A or Class B
def classify_object(feature_vector):
    # Calculate the discriminant function for both classes
    discriminant_A = discriminant_function(feature_vector, mean_class_A, cov_class_A)
    discriminant_B = discriminant_function(feature_vector, mean_class_B, cov_class_B)
    
    # Decide the class with the higher discriminant value
    if discriminant_A > discriminant_B:
        return "Class A"
    else:
        return "Class B"

# Example usage
if __name__ == "__main__":
    # Test data points (feature_1, feature_2)
    test_data_1 = np.array([1, 4])
    test_data_2 = np.array([3, 5])
    
    # Classify the test data points
    result_1 = classify_object(test_data_1)
    result_2 = classify_object(test_data_2)
    
    # Print the results
    print("Test data 1 is classified as:", result_1)
    print("Test data 2 is classified as:", result_2)
