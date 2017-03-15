import os
import json
import requests
import filecmp
import shutil

url = 'https://api.github.com/repos/danbatiste/dsbot/contents/'
blacklisted = ['.\\config.ini', '.\\update.py', '.\\res', '.\\res\\version.json', '.\\update_files', '.\\update_files\\version.json']


def abort_update():
    os.remove('res/version.json')
    with open('update_files/version.json.backup', 'rb') as backup_file:
        with open('res/version.json', 'wb') as file:
            file.write(backup_file.read())
    shutil.rmtree('update_files/')
    print('Update failed.')
    input('Press any key to continue...')
    os._exit(0)


def update(json_url):
    temp_json_dump = requests.get(json_url)
    file_path = 'update_files/' + str(hash(json_url))
    with open(file_path, 'wb') as out_file:
        out_file.write(temp_json_dump.content)

    with open(file_path) as file:
        master = json.load(file)

    for file in master:
        if type(file) == type('str'):
            print('Ratelimit exceeded, please try again later')
            abort_update()
        elif file['type'] == 'file':
            file_url = file['download_url']
            file_dump = requests.get(file_url)
            with open(file['path'], 'wb') as out_file:
                out_file.write(file_dump.content)

        if file['type'] == 'dir':
            update(json_url + file['name'] + '/')


files = requests.get(url, stream=True).raw
if not os.path.exists('update_files'):
    os.mkdir('update_files')
    
with open('update_files/version.json', 'wb') as file:
    shutil.copyfileobj(files, file)


if not os.path.exists('res/version.json'):
    is_current_version = False
    with open('res/version.json', 'wb') as ofile:
        with open('update_files/version.json', 'rb') as ifile:
            ofile.write(ifile.read())
else:
    is_current_version = filecmp.cmp('update_files/version.json','res/version.json')


if not is_current_version:
    with open('res/version.json', 'rb') as file:
        with open('update_files/version.json.backup', 'wb') as backup_file:
            backup_file.write(file.read())

    to_remove = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            f_path = os.path.join(root, file)
            if not f_path in blacklisted:
                try: shutil.rmtree(f_path)
                except: pass

    update(url)
    shutil.rmtree('update_files')
    print('Update succeeded! Bot is now latest version.')
    input('Press any key to continue...')

else:
    shutil.rmtree('update_files/')
    print('Bot is current version!')
    input('Press any key to continue...')
