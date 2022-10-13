import os
import subprocess
import shutil

from pathlib import Path

def test_create_without_gh_prefix():
	subprocess.run(["gh", "py", "create", "test"])
	assert Path("gh-test").exists()
	shutil.rmtree("gh-test")

def test_check_if_executable():
	subprocess.run(["gh", "py", "create", "gh-test"])
	assert Path("gh-test").exists()
	assert os.access("gh-test/gh-test", os.X_OK)
	shutil.rmtree("gh-test")

def test_create_with_space_in_path():
	# make a directory with a space in the name.
	os.mkdir("gh space test")
	os.chdir("gh space test")
	subprocess.run(["gh", "py", "create", "gh-spacer"])
	# install the extension
	subprocess.run(["gh", "extension", "install", "."], shell=False)
	# go back.
	os.chdir("../")
	# call the extension
	subprocess.run(["gh", "spacer", "poetry", "version"], shell=False)
	# remove extension
	subprocess.run(["gh", "extension", "remove", "spacer"], shell=False)
	shutil.rmtree("gh space test")

def test_create_with_gh_prefix():
	subprocess.run(["gh", "py", "create", "gh-test"])
	assert Path("gh-test").exists()
	shutil.rmtree("gh-test")

def test_extension_dir_before_and_after():
	subprocess.run(["gh", "py", "create", "gh-test"])
	os.chdir("gh-test")
	assert not Path(".gh-py").exists()
	assert not Path("poetry.lock").exists()
	subprocess.run(["sh", "gh-test", "-h"], shell=False)
	assert Path(".gh-py").exists()
	assert Path("poetry.lock").exists()
	os.chdir("../")
	shutil.rmtree("gh-test")
