import os


# Write To CSV
def write_to_csv(data, path, file_name='no_name.csv'):
    try:
        os.mkdir(path)
        print("Directory with path '% s' created" % path)
    except:
        print("Directory with path '% s' created" % path)

    data.to_csv(path + '/' + file_name, index=False, header=True)
    print('File wrote to path:', path)
