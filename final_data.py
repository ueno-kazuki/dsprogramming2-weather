from bs4 import BeautifulSoup
import requeｓts

url = "https://www.data.jma.go.jp/obd/stats/etrn/view/daily_a1.php?prec_no=44&block_no=1133&year=2024&month=1&day=9&view="
r = requests.get(url)
r.encoding = 'utf-8'

html_soup = BeautifulSoup(r.text, 'html.parser')

# タグを検索し、条件に一致するものを取得
tag1 = html_soup.find_all('table', class_='data2_s')
# 結果を表示
print(tag1)

# タグを検索し、条件に一致するものを取得
tag2 = html_soup.find_all('td', class_='data_0_0')
# テキストを取得してリストに追加するリスト内包表記を使用
data1 = [tag.string for tag in tag2]

import sqlite3
import os
path = '/Users/uenokazuki/dsprogramming2'  # データベースファイルのディレクトリパス
db_name = 'weather.sqlite'
# データベースファイルの存在チェックと作成
if not os.path.exists(path + db_name):
    # ファイルが存在しない場合は新規に作成
    open(path + db_name, 'w').close()
# データベースに接続
con = sqlite3.connect(path + db_name)
# データベースへの接続を閉じる
con.close()

import sqlite3
# データベースに接続
con = sqlite3.connect(path + db_name)
cur = con.cursor()
# テーブルを作成
cur.execute('CREATE TABLE weather_data (value TEXT)')
# 変更をコミットしてデータベースを閉じる
con.commit()
con.close()

data_to_save = tag2
con = sqlite3.connect(path + db_name)
#sqlを実行するためのオブジェクトを取得
cur = con.cursor()
# データをデータベースに挿入
for item in data_to_save:
    value = item.string
    cur.execute('INSERT INTO weather_data (value) VALUES (?)', (value,))
#必要があればコミットする（データ変更などがあった場合）
con.commit()
con.close()

import sqlite3
# データベースに接続
con = sqlite3.connect(path + db_name)
cur = con.cursor()
# データを選択して表示
cur.execute('SELECT * FROM weather_data')
rows = cur.fetchall()
# 結果を表示
for row in rows:
    print(row)
# データベースを閉じる
con.close()


#ローカルデータ
path = '/Users/uenokazuki/dsprogramming2'
db_name = 'sumaho.sqlite'
#DBに接続する（指定したDBファイルが存在しない場合は、新規に作成される）
con = sqlite3.connect(path + db_name)
#DBへの接続を閉じる
con.close()

con = sqlite3.connect(path + db_name)
#sqlを実行するためのオブジェクトを取得
cur = con.cursor()
#テーブルを作成するsql
sql_create_table ='CREATE TABLE sumaho("エンターテイメント" text, "ゲーム" text, SNS text, "情報と読書" text, "その他" text);'
#sqlを実行する
cur.execute(sql_create_table)
con.close()

con = sqlite3.connect(path + db_name)
#sqlを実行するためのオブジェクトを取得
cur = con.cursor()
#sqlを用意する
sql_insert_many = "INSERT INTO sumaho VALUES (?, ?, ?, ?, ?);"
#データをリストで用意する
#エンターテイメント, ゲーム, SNS, 情報と読書, その他
sumaho_list = [
    ("1時間26分","5時間","1時間57分","1時間30分","3分"),
    ("6時間21分","3時間21分","1時間25分","1分","10分"),
    ("7時間29分","2時間21分","33分","55分","10分"),
    ("3時間53分","4時間48分","1時間16分","9分","31分"),
    ("4時間33分","6時間6分","2時間36分","1時間19分","27分"),
    ("3時間1分","1時間44分","1時間21分","32分","3時間38分"),
    ("5時間30分","1時間40分","3時間15分","17分","5時間16分"),
    ("10時間43分","4時間43分","2時間35分","24分","1時間12分"),
    ("8時間45分","1時間43分","2時間43分","28分","7分"),
    ("6時間57分","3時間33分","1時間7分","0分","3分"),
    ("5時間14分","4時間29分","1時間43分","33分","20分"),
    ("2時間29分","4時間20分","1時間15分","1時間49分","34分"),
]
#sqlを実行する
cur.executemany(sql_insert_many, sumaho_list)
#コミット処理(データ操作を反映させる)
con.commit()
con.close()

con = sqlite3.connect(path + db_name)
#sqlを実行するためのオブジェクトを取得
cur = con.cursor()
#sqlを用意する
sql_select = 'SELECT * FROM sumaho;'
#sqlを実行する
cur.execute(sql_select)
for r in cur:
  print(r)
con.close()

import sqlite3
# データベースに接続
con = sqlite3.connect(path + db_name)
cur = con.cursor()
try:
    # データを選択して表示
    cur.execute('SELECT * FROM sumaho')
    rows = cur.fetchall()
    # 最後の行のデータを表示
    if rows:
        last_row = rows[-1]
        print("Last Row:", last_row)
        # 最後の行を削除（全ての列を条件なしで削除）
        cur.execute('DELETE FROM sumaho WHERE ROWID = (SELECT ROWID FROM sumaho ORDER BY ROWID DESC LIMIT 1)')
        print("Last Row Deleted")
    else:
        print("No Rows in the Table")
except Exception as e:
    print("Error:", e)
finally:
    # データベースを閉じる
    con.commit()
    con.close()

con = sqlite3.connect(path + db_name)
#sqlを実行するためのオブジェクトを取得
cur = con.cursor()
#sqlを用意する
sql_select = 'SELECT * FROM sumaho;'
#sqlを実行する
cur.execute(sql_select)
for r in cur:
  print(r)
con.close()