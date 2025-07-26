function openPortfolioModal(url) {
  const portfolioModal = new bootstrap.Modal('#modal-portfolio', {
    keyboard:false
  });
  const portfolioPreview = document.getElementById("portfolio-preview");
  portfolioPreview.setAttribute("src", url);
  portfolioModal.show();
}
