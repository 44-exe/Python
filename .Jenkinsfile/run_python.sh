echo "WORKSPACE_TMP: $WORKSPACE_TMP"
echo "PWD: $PWD"
python test.py

export WORKSPACE=$(dirname "$0")

BUILDNUM_FILE=$(find $WORKSPACE -name "BUILDNUM.h")
index=0
for BUILDNUM_LINE in `cat $BUILDNUM_FILE | grep --no-ignore-case "#define BUILDNUM"`;
do 
    index=$index+1
    if [[ $index -ge 3 ]]
    then
        index=0
        TMP_BUILD_NUMBER=$BUILDNUM_LINE
    fi
done

export BUILD_NUMBER=$TMP_BUILD_NUMBER
echo "BUILDNUM: $BUILD_NUMBER"


