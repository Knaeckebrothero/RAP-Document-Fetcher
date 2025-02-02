"""
This module holds methods to extract text from images.
"""
import logging as log
import cv2
import pytesseract
from PIL import Image


def ocr_cell(cell_image):
    # Convert to PIL Image for Tesseract
    pil_image = Image.fromarray(cv2.cvtColor(cell_image, cv2.COLOR_BGR2RGB))
    log.debug('Converted cell image to PIL Image')
    # Perform OCR
    text = pytesseract.image_to_string(pil_image)  # , config='--psm 6'
    log.debug(f'Extracted text from cell: {text}')
    return text.strip()
