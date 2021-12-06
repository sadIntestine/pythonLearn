from utils.Log import Log


@Log()
def my_sum(x, y):
    s = 0
    for i in range(x, y + 1):
        s += i
    return s


# 0import lg
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # txt = bug.get_content('https://zzk.cnblogs.com/s/blogpost?Keywords=java&pageindex=1',)
    # result = bug.get_data(txt)
    # bug.write_data(result,'weather.csv')
    # print(txt)10
    # print_hi('Py+Charm')
    # sqliteConnection
    # sqliteConnection.test("夏凡")
    # lg.run_game()
    my_sum(1, 9999999)
