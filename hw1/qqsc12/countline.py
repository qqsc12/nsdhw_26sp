#!/bin/bash

# 1. 處理環境變數與預設值
python_cmd=${PYTHON_BIN:-python3}

# 2. 檢查 Python 執行檔是否存在
if ! command -v "$python_cmd" >/dev/null 2>&1; then
    echo "Error: Specified Python binary '$python_cmd' not found." >&2
    exit 1
fi

# 3. 將 Python 程式碼存在變數中
# 邏輯：讀取所有行 (sys.stdin.readlines) 並計算長度 (len)
_PY_CODE=$(cat << 'EOF'
import sys
data = sys.stdin.readlines()
print(len(data))
EOF
)

# 4. 執行 Python 並將程式碼與參數傳入
exec "$python_cmd" -c "$_PY_CODE" "$@"