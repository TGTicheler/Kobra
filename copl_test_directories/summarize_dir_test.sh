#!/bin/bash
# samenvatten comply info
# vat verschillende records samen tot simpelere tekst
sed -e 's/ASS1MAP,ASS2MAP,ASS3MAP/Heeft alle assignment mappen aangemaakt/' -e 's/ASS1MAKEFILE,ASS2MAKEFILE,ASS3MAKEFILE/Heeft voor iedere assignment een Makefile/'|sed -E 's/ASS([1-3])RUNTARGET,ASS\1BUILDTARGET,ASS\1MAKEFILE/ASS\1COMPLY/g'|sed 's/ASS1COMPLY,ASS2COMPLY,ASS3COMPLY/Complies/'|sed 's/ASS1COMPLY,ASS2COMPLY/1 en 2 complies/'|sed 's/ASS2COMPLY,ASS3COMPLY/2 en 3 complies/'|sed 's/,$//'
