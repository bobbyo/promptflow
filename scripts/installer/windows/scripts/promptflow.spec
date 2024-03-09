# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.utils.hooks import copy_metadata

datas = [('../resources/CLI_LICENSE.rtf', '.'), ('../../../../src/promptflow/NOTICE.txt', '.'),
('../../../../src/promptflow/promptflow/_sdk/data/executable/', './promptflow/_sdk/data/executable/'),
('../../../../src/promptflow-tools/promptflow/tools/', './promptflow/tools/'),
('./pf.bat', '.'), ('./pfs.bat', '.'), ('./pfazure.bat', '.'), ('./pfsvc.bat', '.')]


all_packages = ['pyinstaller-hooks-contrib', 'fixedint', 'gitdb', 'flask-restx', 'typing-extensions', 'waitress', 'greenlet', 'pydeck', 'strictyaml', 'tornado', 'flask-cors', 'six', 'ruamel.yaml.clib', 'deprecated', 'cachetools', 'azure-cosmos', 'werkzeug', 'marshmallow', 'opentelemetry-exporter-otlp-proto-http', 'Jinja2', 'bs4', 'psutil', 'backoff', 'opentelemetry-proto', 'pyrsistent', 'pillow', 'python-dateutil', 'validators', 'jaraco.classes', 'altgraph', 'sqlalchemy', 'cffi', 'blinker', 'pyinstaller', 'setuptools', 'pytz', 'certifi', 'Werkzeug', 'packaging', 'beautifulsoup4', 'regex', 'tzlocal', 'click', 'altair', 'googleapis-common-protos', 'pandas', 'tabulate', 'msal-extensions', 'pydantic', 'keyring', 'numpy', 'distro', 'toml', 'cryptography', 'tqdm', 'filelock', 'azureml-ai-monitoring', 'opentelemetry-api', 'msal', 'Flask', 'msrest', 'watchdog', 'openai', 'sniffio', 'httpcore', 'docutils', 'tiktoken', 'importlib-resources', 'pyarrow', 'filetype', 'azure-monitor-opentelemetry-exporter', 'jsonschema', 'colorama', 'starlette', 'python-dotenv', 'azure-storage-blob', 'streamlit-quill', 'pefile', 'itsdangerous', 'ruamel.yaml', 'httpx', 'aniso8601', 'azure-identity', 'anyio', 'gitpython', 'azure-core', 'azure-storage-file-share', 'requests', 'opentelemetry-sdk', 'protobuf', 'pyyaml', 'fastapi', 'pywin32-ctypes', 'idna', 'azure-ai-ml', 'isodate', 'opentelemetry-exporter-otlp-proto-common', 'azure-storage-file-datalake', 'tenacity', 'streamlit', 'opencensus-ext-azure', 'flask', 'rich', 'importlib-metadata', 'attrs', 'pyjwt', 'pydash', 'azure-common', 'azure-mgmt-core']
meta_packages = ['pyinstaller-hooks-contrib', 'fixedint', 'gitdb', 'flask-restx', 'typing-extensions', 'waitress', 'greenlet', 'pydeck', 'strictyaml', 'tornado', 'flask-cors', 'six', 'ruamel.yaml.clib', 'deprecated', 'cachetools', 'azure-cosmos', 'werkzeug', 'marshmallow', 'opentelemetry-exporter-otlp-proto-http', 'Jinja2', 'bs4', 'psutil', 'opentelemetry-proto', 'pillow', 'python-dateutil', 'jaraco.classes', 'altgraph', 'sqlalchemy', 'cffi', 'blinker', 'pyinstaller', 'setuptools', 'pytz', 'certifi', 'Werkzeug', 'packaging', 'beautifulsoup4', 'regex', 'click', 'altair', 'googleapis-common-protos', 'pandas', 'tabulate', 'msal-extensions', 'pydantic', 'keyring', 'numpy', 'distro', 'toml', 'cryptography', 'tqdm', 'filelock', 'azureml-ai-monitoring', 'opentelemetry-api', 'msal', 'Flask', 'msrest', 'watchdog', 'openai', 'sniffio', 'httpcore', 'docutils', 'tiktoken', 'importlib-resources', 'pyarrow', 'filetype', 'azure-monitor-opentelemetry-exporter', 'jsonschema', 'colorama', 'starlette', 'python-dotenv', 'azure-storage-blob', 'streamlit-quill', 'pefile', 'itsdangerous', 'ruamel.yaml', 'httpx', 'aniso8601', 'azure-identity', 'anyio', 'gitpython', 'azure-core', 'azure-storage-file-share', 'requests', 'opentelemetry-sdk', 'protobuf', 'pyyaml', 'fastapi', 'pywin32-ctypes', 'idna', 'azure-ai-ml', 'isodate', 'opentelemetry-exporter-otlp-proto-common', 'azure-storage-file-datalake', 'tenacity', 'streamlit', 'opencensus-ext-azure', 'flask', 'rich', 'importlib-metadata', 'attrs', 'pyjwt', 'pydash', 'azure-common', 'azure-mgmt-core']

for package in all_packages:
    datas += collect_data_files(package)

for package in meta_packages:
    datas += copy_metadata(package)

datas += collect_data_files('streamlit_quill')
datas += collect_data_files('promptflow')
datas += copy_metadata('promptflow')
hidden_imports = ['win32timezone', 'promptflow'] + ['psutil', 'httpx', 'openai', 'flask', 'sqlalchemy', 'pandas', 'python.dotenv', 'keyring', 'pydash', 'cryptography', 'colorama', 'tabulate', 'filelock', 'marshmallow', 'gitpython', 'tiktoken', 'strictyaml', 'waitress', 'azure.monitor.opentelemetry.exporter', 'ruamel.yaml', 'pyarrow', 'pillow', 'filetype', 'jsonschema', 'docutils', 'opentelemetry.exporter.otlp.proto.http', 'flask_restx', 'flask_cors', 'azure.core', 'azure.storage.blob', 'azure.identity', 'azure.ai.ml', 'pyjwt', 'azure.cosmos', 'pyinstaller', 'streamlit', 'streamlit_quill', 'bs4', 'azure.identity', 'azure.ai.ml', 'azure.monitor.opentelemetry.exporter', 'azureml.ai.monitoring', 'fastapi']

block_cipher = None

pfcli_a = Analysis(
    ['pfcli.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hidden_imports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pfcli_pyz = PYZ(pfcli_a.pure, pfcli_a.zipped_data, cipher=block_cipher)
pfcli_exe = EXE(
    pfcli_pyz,
    pfcli_a.scripts,
    [],
    exclude_binaries=True,
    name='pfcli',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    contents_directory='.',
    icon='../resources/logo32.ico',
    version="./version_info.txt",
)

coll = COLLECT(
    pfcli_exe,
    pfcli_a.binaries,
    pfcli_a.zipfiles,
    pfcli_a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='promptflow',
)
