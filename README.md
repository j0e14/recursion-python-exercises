# recursion-python-exercises

Recursion（新型初級）で自分で解いたPython演習の記録です。最初の公開リポジトリ。

## 第2章「関数」— 文字列操作の演習

`find` で位置を探し、スライスで切り取り、`replace` で置き換える演習です。

| ファイル | 内容 |
|---|---|
| `chapter2/extract_domain.py` | URLからドメイン部分を取り出す（`find` + `len`） |
| `chapter2/get_username.py` | メールアドレスから `@` より前の部分を取り出す |
| `chapter2/make_nickname.py` | 2つの名前の頭2文字ずつを組み合わせてニックネームを作る |
| `chapter2/to_https.py` | `http://` を `https://` に書き換える（`https://` の場合はそのまま返す） |

## 学んだこと

- 文字列は一部分だけを直接書き換えられない。メソッドで新しい文字列を作る
- `find` は「探す対象を、位置という数に変える」もの。スライスには数を渡す
- スライスの範囲は「開始以上・終了未満」
