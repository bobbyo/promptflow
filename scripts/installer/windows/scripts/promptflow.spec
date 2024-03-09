# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.utils.hooks import copy_metadata

datas = [('../resources/CLI_LICENSE.rtf', '.'), ('../../../../src/promptflow/NOTICE.txt', '.'),
('../../../../src/promptflow/promptflow/_sdk/data/executable/', './promptflow/_sdk/data/executable/'),
('../../../../src/promptflow-tools/promptflow/tools/', './promptflow/tools/'),
('./pf.bat', '.'), ('./pfs.bat', '.'), ('./pfazure.bat', '.'), ('./pfsvc.bat', '.')]


all_packages = ['pyrsistent', 'msal', 'pefile', 'pywin32-ctypes', 'pyinstaller-hooks-contrib', 'azure-core', 'streamlit-quill', 'pyjwt', 'attrs', 'Flask', 'httpx', 'waitress', 'httpcore', 'pydantic', 'pyyaml', 'python-dotenv', 'pydeck', 'idna', 'Jinja2', 'opentelemetry-exporter-otlp-proto-common', 'ruamel.yaml.clib', 'altair', 'ruamel.yaml', 'psutil', 'rich', 'gitdb', 'python-dateutil', 'importlib-metadata', 'cffi', 'aniso8601', 'opentelemetry-api', 'click', 'anyio', 'werkzeug', 'flask-restx', 'openai', 'tiktoken', 'azure-cosmos', 'requests', 'pytz', 'azure-monitor-opentelemetry-exporter', 'fixedint', 'regex', 'azure-storage-file-share', 'opentelemetry-proto', 'numpy', 'azure-ai-ml', 'colorama', 'bs4', 'itsdangerous', 'Werkzeug', 'altgraph', 'flask-cors', 'flask', 'streamlit', 'certifi', 'starlette', 'opentelemetry-exporter-otlp-proto-http', 'sqlalchemy', 'blinker', 'toml', 'distro', 'beautifulsoup4', 'jaraco.classes', 'watchdog', 'pyinstaller', 'azure-storage-file-datalake', 'backoff', 'validators', 'pyarrow', 'fastapi', 'pandas', 'typing-extensions', 'opencensus-ext-azure', 'tenacity', 'azure-identity', 'opentelemetry-sdk', 'azureml-ai-monitoring', 'googleapis-common-protos', 'tqdm', 'filetype', 'azure-storage-blob', 'marshmallow', 'packaging', 'tzlocal', 'cachetools', 'pillow', 'pydash', 'importlib-resources', 'sniffio', 'deprecated', 'gitpython', 'msrest', 'isodate', 'six', 'tornado', 'filelock', 'docutils', 'jsonschema', 'keyring', 'cryptography', 'msal-extensions', 'azure-mgmt-core', 'azure-common', 'tabulate', 'greenlet', 'strictyaml', 'protobuf', 'setuptools']
meta_packages = ['msal', 'pefile', 'pywin32-ctypes', 'pyinstaller-hooks-contrib', 'azure-core', 'streamlit-quill', 'pyjwt', 'attrs', 'Flask', 'httpx', 'waitress', 'httpcore', 'pydantic', 'pyyaml', 'python-dotenv', 'pydeck', 'idna', 'Jinja2', 'opentelemetry-exporter-otlp-proto-common', 'ruamel.yaml.clib', 'altair', 'ruamel.yaml', 'psutil', 'rich', 'gitdb', 'python-dateutil', 'importlib-metadata', 'cffi', 'aniso8601', 'opentelemetry-api', 'click', 'anyio', 'werkzeug', 'flask-restx', 'openai', 'tiktoken', 'azure-cosmos', 'requests', 'pytz', 'azure-monitor-opentelemetry-exporter', 'fixedint', 'regex', 'azure-storage-file-share', 'opentelemetry-proto', 'numpy', 'azure-ai-ml', 'colorama', 'bs4', 'itsdangerous', 'Werkzeug', 'altgraph', 'flask-cors', 'flask', 'streamlit', 'certifi', 'starlette', 'opentelemetry-exporter-otlp-proto-http', 'sqlalchemy', 'blinker', 'toml', 'distro', 'beautifulsoup4', 'jaraco.classes', 'watchdog', 'pyinstaller', 'azure-storage-file-datalake', 'pyarrow', 'fastapi', 'pandas', 'typing-extensions', 'opencensus-ext-azure', 'tenacity', 'azure-identity', 'opentelemetry-sdk', 'azureml-ai-monitoring', 'googleapis-common-protos', 'tqdm', 'filetype', 'azure-storage-blob', 'marshmallow', 'packaging', 'cachetools', 'pillow', 'pydash', 'importlib-resources', 'sniffio', 'deprecated', 'gitpython', 'msrest', 'isodate', 'six', 'tornado', 'filelock', 'docutils', 'jsonschema', 'keyring', 'cryptography', 'msal-extensions', 'azure-mgmt-core', 'azure-common', 'tabulate', 'greenlet', 'strictyaml', 'protobuf', 'setuptools']

for package in all_packages:
    datas += collect_data_files(package)

for package in meta_packages:
    datas += copy_metadata(package)

datas += collect_data_files('promptflow')
datas += copy_metadata('promptflow')
hidden_imports = ['win32timezone', 'promptflow', 'opentelemetry'] + ['pyrsistent', 'msal', 'pefile', 'pywin32.ctypes', 'pyinstaller.hooks.contrib', 'azure.core', 'streamlit_quill', 'pyjwt', 'attrs', 'flask', 'httpx', 'waitress', 'httpcore', 'pydantic', 'pyyaml', 'python.dotenv', 'pydeck', 'idna', 'jinja2', 'opentelemetry.exporter.otlp.proto.common', 'ruamel.yaml.clib', 'altair', 'ruamel.yaml', 'psutil', 'rich', 'gitdb', 'python.dateutil', 'importlib.metadata', 'cffi', 'aniso8601', 'opentelemetry.api', 'click', 'anyio', 'werkzeug', 'flask_restx', 'openai', 'tiktoken', 'azure.cosmos', 'requests', 'pytz', 'azure.monitor.opentelemetry.exporter', 'fixedint', 'regex', 'opentelemetry.proto', 'numpy', 'azure.ai.ml', 'colorama', 'bs4', 'itsdangerous', 'werkzeug', 'altgraph', 'flask_cors', 'flask', 'streamlit', 'certifi', 'starlette', 'opentelemetry.exporter.otlp.proto.http', 'sqlalchemy', 'blinker', 'toml', 'distro', 'beautifulsoup4', 'jaraco.classes', 'watchdog', 'pyinstaller', 'backoff', 'validators', 'pyarrow', 'fastapi', 'pandas', 'typing.extensions', 'opencensus.ext.azure', 'tenacity', 'azure.identity', 'opentelemetry.sdk', 'azureml.ai.monitoring', 'googleapis.common.protos', 'tqdm', 'filetype', 'azure.storage.blob', 'marshmallow', 'packaging', 'tzlocal', 'cachetools', 'pillow', 'pydash', 'importlib.resources', 'sniffio', 'deprecated', 'gitpython', 'msrest', 'isodate', 'six', 'tornado', 'filelock', 'docutils', 'jsonschema', 'keyring', 'cryptography', 'msal.extensions', 'azure.mgmt.core', 'azure.common', 'tabulate', 'greenlet', 'strictyaml', 'protobuf', 'setuptools', 'azure.storage.fileshare', 'azure.storage.filedatalake']

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
