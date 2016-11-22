# Copyright 2016 Google Inc. All Rights Reserved.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from smilesparser import SMILES

s = open("test.smi").readlines()
lines = [line.strip().split()[0] for line in s[1:]]
def check(smiles):
  parsed = SMILES.parseString(line)[0]
  if line != parsed and line != str(parsed) and line != str(str(parsed)):
    print "mismatch:"
    print line
    print parsed
    print
    return False
  return True

# from multiprocessing import Pool
# pool = Pool(12)
# results = pool.map(check, lines)
for line in lines:
  check(line)
