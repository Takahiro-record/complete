#import ワークブックと新規作成
#import 日時取得
#import osdata

#変数src_fileに元のファイル「logbook.xlsx」を代入
#やってみる
#wb_srcにsrc_fileを読み込んで代入
#ws_srcはwb_srcのシート「Log」を代入
#失敗したら
#「データを読み込めませんでした」を出力
#作業終了する

#groupsに空の辞書を作成

#ws_srcシートで繰り返し処理を行う(2列目から)
#rowとして読み込んだものをdate_str,category,contentに代入

#もしどれかのデータが不足していたら
#処理を続ける

#やってみる
#yearに日時取得データを代入
#失敗したら「日時形式エラー」と出力
#処理を続ける

#keyにcategoryとyearを代入する
#もしgroupsの中にkeyが不足していたら
#groupsのkeyに空として入力
#groups[key]にdate_strとcontentを追加する

#groupsのアイテムの中身としてcategory,yearを扱い繰り返し処理を行う
#wb_newに新規作成ファイルを代入
#ws_newはwb_newの今開いているシートとする
#そのタイトルは「Log」とする
#ヘッダーとして「日付、内容」を追加する
#itemsの中からdate,contentを抽出する処理を繰り返す
#抽出したdate,contentを追加する

#safe_filenameに「category_year.xlsx」を空白や全角を避けて代入する
#safe_filenameを保存する
#safe_filenameを保存しましたと出力