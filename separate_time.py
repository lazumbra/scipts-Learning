def get_hour_minute(vector_time):
    vector_hours = []
    for hour in vector_time:
        vector_hours.append(hour[:5])
    return vector_hours

vetor_horas = ['09:03:03', '09:18:07', '09:33:12', '09:48:20', '10:03:21', '10:18:22', '10:33:25', '10:48:27', '11:03:28', '11:18:29', '11:33:30', '11:48:31', '12:03:32', '12:18:41', '12:33:44', '12:48:56', '13:03:58', '13:19:02', '13:34:07', '13:49:16', '14:04:17', '14:19:19', '14:34:27', '14:49:28', '15:04:33', '15:19:51', '15:34:52']



new_hours = get_hour_minute(vetor_horas)


print(new_hours)
