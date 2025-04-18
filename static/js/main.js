Dropzone.options.pdfDropzone = {
    paramName: "pdf_file",
    maxFiles: 1,
    acceptedFiles: ".pdf",
    success: function(file, response) {
        // Redirect to the download URL
        window.location.href = response.download_url;
    }
};