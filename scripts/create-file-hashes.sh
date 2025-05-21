for file in dist/*; do
    sha256sum "$file" > "dist/$(basename "$file").sha256"
done