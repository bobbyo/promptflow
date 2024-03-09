# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.utils.hooks import copy_metadata

datas = [('../resources/CLI_LICENSE.rtf', '.'), ('../../../../src/promptflow/NOTICE.txt', '.'),
('../../../../src/promptflow/promptflow/_sdk/data/executable/', './promptflow/_sdk/data/executable/'),
('../../../../src/promptflow-tools/promptflow/tools/', './promptflow/tools/'),
('./pf.bat', '.'), ('./pfs.bat', '.'), ('./pfazure.bat', '.'), ('./pfsvc.bat', '.')]


packages = ['tqdm', 'fixedint', 'altgraph', 'pefile', 'werkzeug', 'Flask', 'toml', 'beautifulsoup4', 'blinker', 'azureml-ai-monitoring', 'typing-extensions', 'greenlet', 'keyring', 'filetype', 'psutil', 'Werkzeug', 'filelock', 'pydeck', 'docutils', 'streamlit-quill', 'flask-cors', 'protobuf', 'tornado', 'waitress', 'marshmallow', 'python-dateutil', 'pydash', 'azure-storage-file-datalake', 'opencensus-ext-azure', 'tzlocal', 'click', 'googleapis-common-protos', 'cryptography', 'azure-cosmos', 'opentelemetry-exporter-otlp-proto-common', 'cachetools', 'pywin32-ctypes', 'flask', 'bs4', 'pyinstaller', 'strictyaml', 'sniffio', 'flask-restx', 'azure-common', 'fastapi', 'requests', 'opentelemetry-proto', 'importlib-resources', 'azure-mgmt-core', 'azure-identity', 'opentelemetry-sdk', 'colorama', 'pydantic', 'cffi', 'pillow', 'certifi', 'packaging', 'pandas', 'tenacity', 'setuptools', 'rich', 'deprecated', 'regex', 'msrest', 'azure-storage-blob', 'ruamel.yaml', 'anyio', 'python-dotenv', 'jaraco.classes', 'importlib-metadata', 'gitpython', 'tiktoken', 'distro', 'pyjwt', 'pyarrow', 'sqlalchemy', 'tabulate', 'msal-extensions', 'opentelemetry-api', 'backoff', 'pyinstaller-hooks-contrib', 'numpy', 'ruamel.yaml.clib', 'azure-ai-ml', 'itsdangerous', 'httpx', 'idna', 'attrs', 'altair', 'aniso8601', 'streamlit', 'pytz', 'starlette', 'azure-core', 'gitdb', 'pyrsistent', 'pyyaml', 'opentelemetry-exporter-otlp-proto-http', 'validators', 'six', 'httpcore', 'azure-storage-file-share', 'watchdog', 'Jinja2', 'openai', 'azure-monitor-opentelemetry-exporter', 'msal', 'isodate', 'jsonschema']

for package in packages:
    datas += copy_metadata(package)
    datas += collect_data_files(package)

datas += collect_data_files('promptflow')
datas += copy_metadata('promptflow')
hidden_imports = [win32timezone', 'promptflow', 'tqdm', 'fixedint', 'altgraph', 'pefile', 'werkzeug', 'Flask', 'toml', 'beautifulsoup4', 'blinker', 'azureml.ai.monitoring', 'typing.extensions', 'greenlet', 'keyring', 'filetype', 'psutil', 'Werkzeug', 'filelock', 'pydeck', 'docutils', 'streamlit_quill', 'flask.cors', 'protobuf', 'tornado', 'waitress', 'marshmallow', 'python.dateutil', 'pydash', 'azure.storage.file.datalake', 'opencensus.ext.azure', 'tzlocal', 'click', 'googleapis.common.protos', 'cryptography', 'azure.cosmos', 'opentelemetry.exporter.otlp.proto.common', 'cachetools', 'pywin32.ctypes', 'flask', 'bs4', 'pyinstaller', 'strictyaml', 'sniffio', 'flask.restx', 'azure.common', 'fastapi', 'requests', 'opentelemetry.proto', 'importlib.resources', 'azure.mgmt.core', 'azure.identity', 'opentelemetry.sdk', 'colorama', 'pydantic', 'cffi', 'pillow', 'certifi', 'packaging', 'pandas', 'tenacity', 'setuptools', 'rich', 'deprecated', 'regex', 'msrest', 'azure.storage.blob', 'ruamel.yaml', 'anyio', 'python.dotenv', 'jaraco.classes', 'importlib.metadata', 'gitpython', 'tiktoken', 'distro', 'pyjwt', 'pyarrow', 'sqlalchemy', 'tabulate', 'msal.extensions', 'opentelemetry.api', 'backoff', 'pyinstaller.hooks.contrib', 'numpy', 'ruamel.yaml.clib', 'azure.ai.ml', 'itsdangerous', 'httpx', 'idna', 'attrs', 'altair', 'aniso8601', 'streamlit', 'streamlit_quill', 'pytz', 'starlette', 'azure.core', 'gitdb', 'pyrsistent', 'pyyaml', 'opentelemetry.exporter.otlp.proto.http', 'validators', 'six', 'httpcore', 'azure.storage.file.share', 'watchdog', 'Jinja2', 'openai', 'azure.monitor.opentelemetry.exporter', 'msal', 'isodate', 'jsonschema']

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
